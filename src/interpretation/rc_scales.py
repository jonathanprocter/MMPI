"""
Restructured Clinical (RC) Scales Interpretations Module

This module provides detailed interpretations for the Restructured Clinical (RC) Scales
of the MMPI-2, with specific narratives for different T-score ranges and gender.
"""

# RC Scales Interpretations Dictionary
RC_SCALES_INTERPRETATIONS = {
    "RCd": {
        "ranges": [
            {
                "range": [0, 64],
                "interpretation": "This woman maintains a generally positive outlook on life. She experiences typical ups and downs but possesses adequate coping resources to manage life's challenges. She sees herself as reasonably competent and effective in most areas of her life. When faced with setbacks, she can mobilize internal and external resources to overcome obstacles. She believes her future holds positive possibilities and can identify specific sources of meaning, purpose, and satisfaction in her life. In daily interactions, she demonstrates an appropriate level of confidence and self-assurance without excessive self-doubt. Her emotional experiences include a full range of both positive and negative feelings, with neither dominating her overall experience."
            },
            {
                "range": [65, 65],
                "interpretation": "This woman is beginning to question her ability to cope effectively with life's demands. She expresses a growing sense that things aren't going well in several areas of her life simultaneously. She reports periods of feeling overwhelmed and uncertain about the future. Her self-confidence is becoming fragile, particularly when facing new challenges. She experiences more frequent episodes of self-doubt and questions her decisions more often. While she can still identify some areas of satisfaction and competence, these positive aspects are increasingly overshadowed by a generalized sense of discouragement. She describes a gradual erosion of hope and optimism that is beginning to affect her motivation and engagement with previously meaningful activities."
            },
            {
                "range": [66, 120],
                "interpretation": "This woman experiences profound and pervasive demoralization that colors virtually all aspects of her life. She describes a deep sense of helplessness and hopelessness, believing that her situation cannot improve regardless of her efforts. Her narrative is dominated by themes of failure, inadequacy, and defeat. She struggles to identify any significant sources of satisfaction or meaning in her life. Daily activities feel burdensome and purposeless. She expresses a conviction that she fundamentally lacks the capabilities necessary to handle life's demands, leading to a pattern of avoidance and withdrawal. Her self-perception is characterized by worthlessness and incompetence. She describes feeling trapped in her current circumstances with no viable path forward. This pervasive demoralization serves as a foundation for her other specific symptoms and significantly impairs her functioning across multiple domains."
            }
        ]
    },
    "RC1": {
        "ranges": [
            {
                "range": [0, 64],
                "interpretation": "This woman reports generally good physical health with typical minor ailments that resolve appropriately. She notices bodily sensations but doesn't fixate on them or interpret them catastrophically. When illness occurs, she seeks appropriate medical care without excessive health-related worry. Her narrative about her physical functioning is balanced and realistic. She acknowledges occasional discomforts but doesn't organize her life around physical symptoms or limitations. Her identity isn't significantly connected to health status, and she can engage in activities without undue concern about physical capabilities or possible symptom exacerbation. She readily shifts her attention away from bodily sensations to focus on external interests and relationships."
            },
            {
                "range": [65, 65],
                "interpretation": "This woman is becoming increasingly focused on bodily sensations and physical health concerns. She reports multiple physical symptoms that may exceed medical findings or have fluctuating presentation. She describes spending more time thinking about her health and researching potential explanations for her physical discomfort. Medical appointments are becoming more frequent as she seeks validation and explanation for her symptoms. She expresses frustration when medical evaluations don't yield clear diagnoses or effective treatments. In daily life, she is beginning to limit certain activities due to anticipated physical discomfort or fatigue. Conversations increasingly include references to her health status and physical complaints. She is developing a pattern of hypervigilance to bodily sensations, which intensifies her awareness of normal physiological variations."
            },
            {
                "range": [66, 120],
                "interpretation": "This woman's experience is dominated by multiple, persistent somatic complaints affecting various body systems. She describes debilitating symptoms including pain, weakness, gastrointestinal distress, and neurological complaints that significantly impair her daily functioning. Her narrative centers around her physical suffering, medical appointments, and the search for diagnosis and relief. She expresses deep frustration with healthcare providers who she feels haven't properly acknowledged or addressed her symptoms. Her identity has become increasingly organized around being ill, and she spends significant time researching conditions that might explain her experiences. She has substantially curtailed work, family, and social activities due to physical limitations and fatigue. She describes a constant state of bodily monitoring and can provide elaborate details about symptom patterns, intensities, and triggers. Despite multiple medical evaluations with limited findings, she remains convinced that undiscovered physical pathology explains her suffering."
            }
        ]
    },
    "RC2": {
        "ranges": [
            {
                "range": [0, 64],
                "interpretation": "This woman describes a life that includes genuine experiences of joy, enthusiasm, and satisfaction. She can become excited about future events and anticipates pleasure from activities and relationships. She readily identifies specific sources of happiness in her life and recounts recent experiences of enjoyment with appropriate emotional animation. Her affect during interviews shows normal range and modulation, with spontaneous smiles and expressions of positive emotion when discussing pleasant topics. She maintains engagement in activities specifically for their pleasurable qualities and can identify hobbies or interests that reliably bring her satisfaction. Her social relationships include shared enjoyment and positive emotional exchanges."
            },
            {
                "range": [65, 65],
                "interpretation": "This woman is beginning to experience a noticeable diminishment in positive emotions. She describes less frequent experiences of joy or enthusiasm and notes that activities that once brought reliable pleasure now feel less satisfying. While not actively unhappy, she reports a growing sense of emotional flatness or neutrality. She has difficulty generating anticipatory excitement for future events and describes having to 'go through the motions' in situations where she previously felt genuine enthusiasm. Her affect during interviews shows less spontaneous animation, with fewer natural smiles or expressions of positive emotion. She reports reduced initiation of pleasurable activities as the anticipated reward no longer seems worth the effort. She may describe this experience as 'the color draining from life' while not feeling overtly sad."
            },
            {
                "range": [66, 120],
                "interpretation": "This woman experiences a profound and pervasive absence of positive emotions that fundamentally alters her experience of life. She describes an inability to feel joy, pleasure, or enthusiasm in any context, even when good things happen. Her emotional landscape is characterized by flatness, emptiness, and anhedonia rather than active sadness. She expresses no anticipatory pleasure for future events and cannot imagine experiencing genuine happiness again. Activities that logically should bring satisfaction feel hollow and meaningless. Her affect during interviews is notably restricted, with an absence of spontaneous positive expressions and limited emotional range. She has abandoned previously enjoyed activities as they no longer provide any sense of satisfaction. Her descriptions of relationships and experiences lack emotional vibrancy, focusing instead on mechanical aspects of interactions. This profound capacity deficit for positive emotions has led to a colorless, two-dimensional experience of life that she finds profoundly alienating and difficult to convey to others."
            }
        ]
    },
    "RC3": {
        "ranges": [
            {
                "range": [0, 64],
                "interpretation": "This woman maintains a generally balanced view of human nature, acknowledging both positive and negative potentials in others. She forms trusting relationships while maintaining appropriate boundaries and caution with unfamiliar people. She generally takes others at face value without looking for hidden agendas or manipulation. She views most social interactions as straightforward rather than laden with deception. When others treat her well, she accepts their kindness as genuine rather than questioning their motives. She anticipates that most people will be fair and reasonable in their dealings with her. Her relationships are characterized by appropriate openness and vulnerability rather than defensive self-protection."
            },
            {
                "range": [65, 65],
                "interpretation": "This woman is developing a more guarded and skeptical orientation toward others. She increasingly questions others' motives and looks for hidden agendas in their behavior. She describes becoming more alert to potential manipulation or exploitation in relationships. She reports feeling more cautious about trusting others with personal information or vulnerabilities. She is beginning to interpret neutral or ambiguous social cues as potentially threatening or deceptive. She expresses growing concern that others may take advantage of her if given the opportunity. Her relationships are becoming characterized by greater vigilance and emotional distance as self-protection. She describes feeling increasingly alone in a world she perceives as increasingly filled with self-interest and potential betrayal."
            },
            {
                "range": [66, 120],
                "interpretation": "This woman maintains a pervasive and entrenched cynicism about human nature and relationships. She approaches virtually all interactions with the expectation of manipulation, exploitation, or betrayal. She describes a worldview in which most people operate from purely self-interested motives and will readily take advantage of others when possible. She maintains vigilant attention to potential signs of deception or hidden agendas in others' behavior. She reports minimal trust in close relationships and maintains significant emotional distance as self-protection. She interprets neutral or positive social cues through a lens of suspicion, often attributing malevolent intentions to benign behaviors. She describes feeling fundamentally alone in a hostile world where genuine connection is rare or impossible. Her relationships are characterized by guardedness, emotional withholding, and anticipation of eventual betrayal. This pervasive cynicism serves as both a worldview and a defensive strategy that significantly limits her capacity for intimacy and authentic connection."
            }
        ]
    }
}

def get_rc_scale_interpretation(scale, t_score, gender):
    """
    Get the interpretation for an RC scale based on T-score and gender.
    
    Args:
        scale (str): The RC scale code (e.g., "RCd", "RC1", "RC2")
        t_score (int): The T-score value
        gender (str): "Male" or "Female"
        
    Returns:
        str: The appropriate interpretation text based on T-score range
    """
    if scale not in RC_SCALES_INTERPRETATIONS:
        return f"Interpretation not available for scale: {scale}"
    
    scale_dict = RC_SCALES_INTERPRETATIONS[scale]
    
    if "ranges" in scale_dict:
        for range_info in scale_dict["ranges"]:
            min_val, max_val = range_info["range"]
            if min_val <= t_score <= max_val:
                return range_info["interpretation"]
    
    return f"No interpretation available for {scale} with T-score {t_score}"ection.",
        
        "moderate": "This woman is developing increasingly cynical attitudes about others' motives and intentions. She expresses growing skepticism about the genuineness of others' expressed feelings and describes looking for 'the real reason' behind people's actions. She reports becoming more guarded in relationships and less willing to take others at face value. Her narrative includes more frequent references to times she has been disappointed or taken advantage of by others. She describes a shift toward expecting potential exploitation or manipulation in new relationships. In social situations, she finds herself becoming more observant of potential signs of insincerity or deception. While not completely mistrustful, she expresses a growing conviction that most people are primarily self-interested and will exploit others when convenient.",
        
        "high": "This woman's worldview is dominated by profound cynicism and mistrust regarding human nature and relationships. She expresses absolute conviction that people are fundamentally selfish, dishonest, and exploitative. She interprets virtually all social interaction through a lens of suspicion, looking for hidden agendas and manipulation even in seemingly benign exchanges. She describes maintaining vigilant emotional distance in relationships to protect herself from inevitable betrayal. Her narrative is filled with examples of others' moral failings, deceptions, and exploitation, which she sees as confirming her cynical worldview. She expresses contempt for those who maintain 'naive' trust in others' goodness. In daily interactions, she scrutinizes others' statements for inconsistencies and signs of deception, remaining constantly on guard. This pervasive cynicism creates significant interpersonal distance as she refuses to risk vulnerability, leading to superficial connections characterized by emotional detachment and lack of genuine intimacy."
    },
    
    "RC4": {
        "low": "This woman generally conforms to social norms and expectations. She describes a developmental history without significant behavioral problems or authority conflicts. Her narrative demonstrates respect for rules and laws, which she views as necessary for social functioning. She makes decisions with consideration for potential consequences and ethical implications. Her relationships are characterized by appropriate boundaries and consideration for others' rights and feelings. She demonstrates impulse control and can delay gratification appropriately. If she has experimented with substances, it has been within normative patterns without progression to problematic use. Her work history shows appropriate reliability and responsibility.",
        
        "moderate": "This woman reports a history that includes some rule-breaking behavior and authority conflicts, particularly during adolescence. She describes instances of rebelliousness that exceeded typical dev
(Content truncated due to size limit. Use line ranges to read in chunks)
