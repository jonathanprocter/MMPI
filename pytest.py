import sys
import os
import importlib
import inspect
import argparse


# minimal fixture decorator
def fixture(func):
    func._is_fixture = True
    return func


def _call_fixture(func):
    res = func()
    if inspect.isgenerator(res):
        gen = res
        try:
            value = next(gen)
        except StopIteration:
            value = None
        return value, gen
    return res, None


def run_tests(paths):
    total = 0
    failed = 0
    for path in paths:
        modules = []
        if os.path.isdir(path):
            for fname in sorted(os.listdir(path)):
                if fname.startswith('test') and fname.endswith('.py'):
                    mod_name = f"{path}.{fname[:-3]}".replace('/', '.')
                    modules.append(importlib.import_module(mod_name))
        elif path.endswith('.py'):
            mod_name = path[:-3].replace('/', '.')
            modules.append(importlib.import_module(mod_name))
        for module in modules:
            fixtures = {name: obj for name, obj in vars(module).items() if getattr(obj, '_is_fixture', False)}
            tests = [(name, obj) for name, obj in vars(module).items() if name.startswith('test_') and callable(obj)]
            for name, test in tests:
                sig = inspect.signature(test)
                args = []
                gens = []
                for param in sig.parameters.values():
                    f = fixtures.get(param.name)
                    if f is None:
                        raise TypeError(f"Fixture '{param.name}' not found for {name}")
                    value, gen = _call_fixture(f)
                    args.append(value)
                    if gen is not None:
                        gens.append(gen)
                try:
                    test(*args)
                    total += 1
                except AssertionError as e:
                    failed += 1
                    total += 1
                    print(f"{name}: FAIL ({e})")
                except Exception as e:
                    failed += 1
                    total += 1
                    print(f"{name}: ERROR ({e})")
                finally:
                    for gen in gens:
                        try:
                            next(gen)
                        except StopIteration:
                            pass
    if failed:
        print(f"{total - failed} passed, {failed} failed")
    else:
        print(f"{total} passed")
    return failed == 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', action='store_true', dest='quiet')
    parser.add_argument('paths', nargs='*')
    args = parser.parse_args(argv)
    paths = args.paths or ['tests']
    success = run_tests(paths)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
