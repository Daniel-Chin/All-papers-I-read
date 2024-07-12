from __future__ import annotations

from typing import List, Optional
from dataclasses import dataclass

import tags
from tags import *

@dataclass
class Paper:
    shorts: Optional[List[str]]
    apa: Optional[str]
    bib: Optional[str]
    abstract: Optional[str]
    tags: Optional[List[Tag]]
    my_notes: Optional[str]

    def __init__(
        self, shorts=None, apa=None, bib=None, abstract=None, 
        tags=None, my_notes=None, 
    ):
        self.shorts = shorts
        self.apa = apa
        self.bib = bib
        self.abstract = abstract
        self.tags = tags
        self.my_notes = my_notes

def allPapers():
    s = []
    tags_and_more = set(tags.__dict__.keys())
    for key, value in globals().items():
        if key.startswith('__'):
            continue
        if key in [
            'allPapers', 'Paper', 'tags', 
            'annotations', 'Optional', 'List', 'dataclass', 
        ]:
            continue
        if key in tags_and_more:
            continue
        s.append((key, value))
    return s

theme_transformer = Paper(
    apa = r'''Shih, Y. J., Wu, S. L., Zalkow, F., Müller, M., & Yang, Y. H. (2021). Theme Transformer: Symbolic Music Generation with Theme-Conditioned Transformer. arXiv preprint arXiv:2111.04093.''', 
    bib = r'''@article{shih2021theme,
  title={Theme Transformer: Symbolic Music Generation with Theme-Conditioned Transformer},
  author={Shih, Yi-Jen and Wu, Shih-Lun and Zalkow, Frank and M{\"u}ller, Meinard and Yang, Yi-Hsuan},
  journal={arXiv preprint arXiv:2111.04093},
  year={2021}
}''', 
    abstract = r'''Attention-based Transformer models have been increasingly employed for automatic music generation. To condition the generation process of such a model with a user-specified sequence, a popular approach is to take that conditioning sequence as a priming sequence and ask a Transformer decoder to generate a continuation. However, this prompt-based conditioning cannot guarantee that the conditioning sequence would develop or even simply repeat itself in the generated continuation. In this paper, we propose an alternative conditioning approach, called theme-based conditioning, that explicitly trains the Transformer to treat the conditioning sequence as a thematic material that has to manifest itself multiple times in its generation result. This is achieved with two main technical contributions. First, we propose a deep learning-based approach that uses contrastive representation learning and clustering to automatically retrieve thematic materials from music pieces in the training data. Second, we propose a novel gated parallel attention module to be used in a sequence-to-sequence (seq2seq) encoder/decoder architecture to more effectively account for a given conditioning thematic material in the generation process of the Transformer decoder. We report on objective and subjective evaluations of variants of the proposed Theme Transformer and the conventional prompt-based baseline, showing that our best model can generate, to some extent, polyphonic pop piano music with repetition and plausible variations of a given condition.''', 
    tags = [transformer, music_knowledge, contrastive], 
)

Melon_form_then_content = Paper(
    apa = r'''Zou, Y., Zou, P., Zhao, Y., Zhang, K., Zhang, R., & Wang, X. (2021). MELONS: generating melody with long-term structure using transformers and structure graph. arXiv preprint arXiv:2110.05020.''', 
    bib = r'''@article{zou2021melons,
  title={MELONS: generating melody with long-term structure using transformers and structure graph},
  author={Zou, Yi and Zou, Pei and Zhao, Yi and Zhang, Kaixiang and Zhang, Ran and Wang, Xiaorui},
  journal={arXiv preprint arXiv:2110.05020},
  year={2021}
}''', 
    abstract = r'''The creation of long melody sequences requires effective expression of coherent musical structure. However, there is no clear representation of musical structure. Recent works on music generation have suggested various approaches to deal with the structural information of music, but generating a full-song melody with clear long-term structure remains a challenge. In this paper, we propose MELONS, a melody generation framework based on a graph representation of music structure which consists of eight types of bar-level relations. MELONS adopts a multi-step generation method with transformer-based networks by factoring melody generation into two sub-problems: structure generation and structure conditional melody generation. Experimental results show that MELONS can produce structured melodies with high quality and rich contents.
''', 
    tags = [hierarchical, generation, structure, relation, music_knowledge, transformer], 
    my_notes = r'''
This is my Q&A. 
Using one model to predict conditional, instead of one model for each relation type, is because assuming shared knowledge? 
why seperate conditional against unconditional, but not seperate the relation types? 
    unconditional does not see "related measure", so the problem is utterly different. 

uncondition: trained only on no-relation? 
    no, trained on every bar. 
    after generation, structure graph becomes different? 
        on one hand, generation failure e.g. transposition
        on the other hand, spontaneously occuring relations?
        Yes. This happens. 

measure ID order anomoly? 
    the generation of related bar ID can see the current bar ID. 
    DUring inference, we use rejection sampling. 

did you try making the relation model attend to melody of first 8? 
    they are thinking about that. 

my notes
    Again! we see reducing a relation graph to binary relations. 
''', 
)

KLI = Paper(
    apa = r'''Koedinger, K. R., Corbett, A. T., & Perfetti, C. (2012). The Knowledge‐Learning‐Instruction framework: Bridging the science‐practice chasm to enhance robust student learning. Cognitive science, 36(5), 757-798.''', 
    bib = r'''@article{koedinger2012knowledge,
  title={The Knowledge-Learning-Instruction framework: Bridging the science-practice chasm to enhance robust student learning},
  author={Koedinger, Kenneth R and Corbett, Albert T and Perfetti, Charles},
  journal={Cognitive science},
  volume={36},
  number={5},
  pages={757--798},
  year={2012},
  publisher={Wiley Online Library}
}''', 
    abstract = None, 
    tags = [psychology, education], 
    my_notes = r'''
Fig.1 (P5)
    - explain fig. 
    - learning events as a subset of instructional events. 
    - adaptive moments. 
    - Ziyu, when testing CYP, said "at that moment, i was deeply surprised, and learned something." (12/13 notes)
    
    IE is more observable than LE. 
    IE is temporal (1D). LE and KC are structural (hierachical). (This is my interpretation of the paper)
    
    typical experiments are end-to-end: vary IE, compare AE. 
"Many efforts at instructional ‘‘theory’’ are really frameworks (e.g., Bloom, 1956; Gagne,1985; van Merrie¨nboer & Sweller, 2005; Sweller & Chandler, 1994) because they do not lead directly to precise predictions." (P4)
    金三角非理论，框架也。
Table 2
    paper 支持 KC 作为单元。可能不确切，但可以让教育更加量化，可以设计实验。
        music 如何 提取、提出 KC? 
    table 2 是各种 KC 的一个 principal dimensions. 
        music KC with contant/variable io? 
table 3 (page 11)
    go over the table. 
    KC can be verbal or nonverbal. 
"Verbal instruction is intrinsically bound to learning verbal KCs."
    traditional music instruction is *verbal*. 
        打开！
        手指自信地下落但是力度要轻！
    but music production is hardly a verbal process. 
        unlike math, history, science, music is a less verbal area. 
    to be fair, verbal articulation usually helps learning. e.g. self-explanation boosts the learning effect. If our system is an expansion of instructional modalities, we should not drop verbal? 
Human overfit. 
    "students may acquire incorrectly generalized conditions" (P17)
    AE must detect that. 
    We can test this in user study - an interesting learning outcome. 
Intruction mode is KC-specific, not domain-specific (P18)
Fig.3 (P20)
    先看三个定义。 (P19)
    再看表。
    U&S: 模进是什么
    I&R: 不同 mode 的模进都是模进。听模进和写模进。
    M&F: proficiency
    related to system 1 system 2. 
    学者，藏焉，修焉，息焉，游焉
    Can a learner arrive at verbal conclusions just from multi-modal training? 
        we can test verbal knowledge of the subjects. e.g. is the green note E4? 
        unsupervised pre-training
table 5 (P25)
    过一遍。可能相关性不高
    例题, 习题 - force, adaptive
''', 
)

Jukebox = Paper(
    apa = r'''Dhariwal, P., Jun, H., Payne, C., Kim, J. W., Radford, A., & Sutskever, I. (2020). Jukebox: A generative model for music. arXiv preprint arXiv:2005.00341.''', 
    bib = r'''@article{dhariwal2020jukebox,
  title={Jukebox: A generative model for music},
  author={Dhariwal, Prafulla and Jun, Heewoo and Payne, Christine and Kim, Jong Wook and Radford, Alec and Sutskever, Ilya},
  journal={arXiv preprint arXiv:2005.00341},
  year={2020}
}
''', 
    abstract = r'''We introduce Jukebox, a model that generates music with singing in the raw audio domain. We tackle the long context of raw audio using a multi-scale VQ-VAE to compress it to discrete codes, and modeling those using autoregressive Transformers. We show that the combined model at scale can generate high-fidelity and diverse songs with coherence up to multiple minutes. We can condition on artist and genre to steer the musical and vocal style, and on unaligned lyrics to make the singing more controllable. We are releasing thousands of non cherry-picked samples at this https URL, along with model weights and code at this https URL''', 
    tags = [generation, vq_vae], 
    my_notes = r'''
Transformer over VQ-VAE. Supervised with lyrics as condition. 
''', 
)

SPICE = Paper(
    apa = r'''Gfeller, B., Frank, C., Roblek, D., Sharifi, M., Tagliasacchi, M., & Velimirović, M. (2020). SPICE: Self-supervised pitch estimation. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 28, 1118-1128.''', 
    bib = r'''@article{gfeller2020spice,
  title={SPICE: Self-supervised pitch estimation},
  author={Gfeller, Beat and Frank, Christian and Roblek, Dominik and Sharifi, Matt and Tagliasacchi, Marco and Velimirovi{\'c}, Mihajlo},
  journal={IEEE/ACM Transactions on Audio, Speech, and Language Processing},
  volume={28},
  pages={1118--1128},
  year={2020},
  publisher={IEEE}
}
''', 
    abstract = r'''We propose a model to estimate the fundamental frequency in monophonic audio, often referred to as pitch estimation. We acknowledge the fact that obtaining ground truth annotations at the required temporal and frequency resolution is a particularly daunting task. Therefore, we propose to adopt a self-supervised learning technique, which is able to estimate pitch without any form of supervision. The key observation is that pitch shift maps to a simple translation when the audio signal is analysed through the lens of the constant-Q transform (CQT). We design a self-supervised task by feeding two shifted slices of the CQT to the same convolutional encoder, and require that the difference in the outputs is proportional to the corresponding difference in pitch. In addition, we introduce a small model head on top of the encoder, which is able to determine the confidence of the pitch estimate, so as to distinguish between voiced and unvoiced audio. Our results show that the proposed method is able to estimate pitch at a level of accuracy comparable to fully supervised models, both on clean and noisy audio samples, although it does not require access to large labeled datasets.''', 
    tags = [self_supervise, f0, pitch_shift_invariance], 
    my_notes = r'''
This works??? What the heck
''', 
)

improving_music_performance_assessment_with_contrastive_learning = Paper(
    apa = r'''Seshadri, P., & Lerch, A. (2021). Improving Music Performance Assessment with Contrastive Learning. arXiv preprint arXiv:2108.01711.''', 
    bib = r'''@article{seshadri2021improving,
  title={Improving Music Performance Assessment with Contrastive Learning},
  author={Seshadri, Pavan and Lerch, Alexander},
  journal={arXiv preprint arXiv:2108.01711},
  year={2021}
}
''', 
    abstract = r'''Several automatic approaches for objective music performance assessment (MPA) have been proposed in the past, however, existing systems are not yet capable of reliably predicting ratings with the same accuracy as professional judges. This study investigates contrastive learning as a potential method to improve existing MPA systems. Contrastive learning is a widely used technique in representation learning to learn a structured latent space capable of separately clustering multiple classes. It has been shown to produce state of the art results for image-based classification problems. We introduce a weighted contrastive loss suitable for regression tasks applied to a convolutional neural network and show that contrastive loss results in performance gains in regression tasks for MPA. Our results show that contrastive-based methods are able to match and exceed SoTA performance for MPA regression tasks by creating better class clusters within the latent space of the neural networks.
''', 
    tags = [contrastive], 
    my_notes = r'''''', 
)

PianoTouch = Paper(
    apa = r'''Huang, K., Do, E. Y. L., & Starner, T. (2008, September). PianoTouch: A wearable haptic piano instruction system for passive learning of piano skills. In 2008 12th IEEE international symposium on wearable computers (pp. 41-44). IEEE.''', 
    bib = r'''@inproceedings{huang2008pianotouch,
  title={PianoTouch: A wearable haptic piano instruction system for passive learning of piano skills},
  author={Huang, Kevin and Do, Ellen Yi-Luen and Starner, Thad},
  booktitle={2008 12th IEEE international symposium on wearable computers},
  pages={41--44},
  year={2008},
  organization={IEEE}
}
''', 
    abstract = r'''We present PianoTouch, a wearable, wireless haptic piano instruction system, composed of (1) five small vibration motors, one for each finger, fitted inside a glove, (2) a Bluetooth module mounted on the glove, and (3) piano music output from a laptop. Users hear the piano music and feel the vibrations indicating which finger is used to play the note. We investigate the system's potential for passive learning, i.e. learning piano playing automatically while engaged in everyday activities. In a preliminary study, four subjects learned two songs initially and then wore the PianoTouch glove for 30 minutes while listening to the songs repeated. One of the songs included tactile sensations and the other did not. The study found that after 30 minutes, the PianoTouch subjects were able to play the song accompanied by tactile sensations better than the non-tactile song. These results suggest the value of a more detailed study.
''', 
    tags = [haptic, vibration, passive_learning, music_edu], 
    my_notes = r'''
Summary: user testing shows passive vibration input helps retain a song after learning it first. 
Q: During active learning, was there a score? During testing, was there a score? 
''', 
)

developing_a_haptic_glove_for_basic_piano_education = Paper(
    apa = r'''Pala, F. K. (2019). Developing a haptic glove for basic piano education. World Journal on Educational Technology: Current Issues, 11(1), 38-47.''', 
    bib = r'''@article{pala2019developing,
  title={Developing a haptic glove for basic piano education},
  author={Pala, Ferhat Kadir and others},
  journal={World Journal on Educational Technology: Current Issues},
  volume={11},
  number={1},
  pages={38--47},
  year={2019}
}
''', 
    abstract = None, 
    tags = [haptic, music_edu], 
    my_notes = r'''Hardly a good paper.''', 
)

visiohaptic_trace_shape_longterm = Paper(
    apa = r'''Yang, X. D., Bischof, W. F., & Boulanger, P. (2008, March). Validating the performance of haptic motor skill training. In 2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems (pp. 129-135). IEEE.''', 
    bib = r'''@inproceedings{yang2008validating,
  title={Validating the performance of haptic motor skill training},
  author={Yang, Xing-Dong and Bischof, Walter F and Boulanger, Pierre},
  booktitle={2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems},
  pages={129--135},
  year={2008},
  organization={IEEE}
}
''', 
    abstract = r'''The effect of haptic interfaces on motor skill training has been widely studied. However, relatively little is known about whether haptic training can promote long-term motor skill acquisition. In this paper, we report two experimental studies that investigated the effectiveness of visuohaptic (visual + haptic) interfaces in helping people develop short-term and long-term motor skills. Our first study compared training outcomes of visuohaptic training, visual training, and no-assistance training. We found that the training outcomes for the tested methods were similar when helping participants develop short-term motor skills. Our second experiment assessed the potential of visual training and visuohaptic training in promoting the development of long-term motor skills. Participants were trained during a four-day-long period. The results showed that the participants gained long-term skills through both training methods, and that the training outcomes for both methods were similar. The results also showed that visuohaptic training is a promising method, but that it needs to be further developed to be useful.''', 
    tags = [haptic, visual, multimodal, adaptive_curriculum_scaffolding], 
    my_notes = r'''
Maybe: 
    making a mistake and being corrected does not backprop.
    only actively correcting one's mistake backprops. 
paper: 
    passive learning -> less effort -> learn less
    "dynamically modify guidance ... according to the learner's skill level."
- Their visual is CYP overlaid onto ground truth. 
''', 
)

drum_haptic_audio = Paper(
    apa = r'''Grindlay, G. (2008, March). Haptic guidance benefits musical motor learning. In 2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems (pp. 397-404). IEEE.''', 
    bib = r'''@inproceedings{grindlay2008haptic,
  title={Haptic guidance benefits musical motor learning},
  author={Grindlay, Graham},
  booktitle={2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems},
  pages={397--404},
  year={2008},
  organization={IEEE}
}
''', 
    abstract = r'''This paper presents the results of a pilot experiment looking at the effect of haptic guidance on musical training. A percussion performance task was used where subjects learned to play short rhythmic sequences on a device capable of recording drumstick movements with a high degree of spatiotemporal accuracy. Subjects learned to perform the sequences under three primary training paradigms: listening to the rhythm (audio), being guided through the motions involved in the rhythm's performance (haptic), and being guided through the required motions while listening to the resulting sound (audio+haptic). Performance was assessed in terms of both timing and loudness (velocity) accuracy using several different metrics. Results indicate that haptic guidance can significantly benefit recall of both note timing and velocity. When subject performance was compared in terms of note velocity recall, the addition of haptic guidance to audio-based training produced a 17% reduction in final error when compared to audio training alone. When performance was evaluated in terms of liming recall, the combination of audio and haptic guidance led to an 18% reduction in early-stage error.''', 
    tags = [haptic, audio, multimodal, music_edu], 
    my_notes = r'''Nice engineering and stats.''', 
)

three_d_trajectory_haptic = Paper(
    apa = r'''Feygin, D., Keehner, M., & Tendick, R. (2002, March). Haptic guidance: Experimental evaluation of a haptic training method for a perceptual motor skill. In Proceedings 10th Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems. HAPTICS 2002 (pp. 40-47). IEEE.''', 
    bib = r'''@inproceedings{feygin2002haptic,
  title={Haptic guidance: Experimental evaluation of a haptic training method for a perceptual motor skill},
  author={Feygin, David and Keehner, Madeleine and Tendick, R},
  booktitle={Proceedings 10th Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems. HAPTICS 2002},
  pages={40--47},
  year={2002},
  organization={IEEE}
}
''', 
    abstract = r'''In this paper we investigate a use of haptics for skills training which we call haptic guidance. In the haptic guidance paradigm, the subject is physically guided through the ideal motion by the haptic interface, thus giving the subject a kinesthetic understanding of what is required. Subjects learned a complex 3D motion under three training conditions (haptic, visual, haptic and visual) and were required to manually reproduce the movement under two recall conditions (with vision, without vision). Performance was measured in terms of position, shape, timing, and drift. Findings from this study indicate that haptic guidance is effective in training. While visual training was better for teaching the trajectory shape, temporal aspects of the task were more effectively learned from haptic guidance. This supports a possible role for haptics in the training of perceptual motor skills in virtual environments.''', 
    tags = [haptic, visual, multimodal], 
    my_notes = r'''
Cite: 
    haptic guidance: "the subject is physically guided through the ideal motion by the haptic interface, thus giving the subject a kinesthetic understanding of what is required."
- abstract highlight: H is better for rhythm and V for trajectory. 
- Their visual is only ground truth, no interactivity. 
- 学 H (眼睛遮住) 测 H+V (眼睛睁开) 的分数比 测 H (眼睛遮住) 分数低。"This suggests that vision may somehow interfere with the haptic representation of the task."
Q: 为什么 V training phase 只是观察 ground truth, 没有同时动手？这才导致了 V vs H 与 observation vs practice 耦合了？
''', 
)

MoveMe_haptic_guide_theremin = Paper(
    apa = r'''Fujii, K., Russo, S. S., Maes, P., & Rekimoto, J. (2015, November). MoveMe: 3D haptic support for a musical instrument. In Proceedings of the 12th International Conference on Advances in Computer Entertainment Technology (pp. 1-8).''', 
    bib = r'''@inproceedings{fujii2015moveme,
  title={MoveMe: 3D haptic support for a musical instrument},
  author={Fujii, Katsuya and Russo, Sophia S and Maes, Pattie and Rekimoto, Jun},
  booktitle={Proceedings of the 12th International Conference on Advances in Computer Entertainment Technology},
  pages={1--8},
  year={2015}
}
''', 
    abstract = r'''Fine motor skills like finger/hand manipulations are essential for playing musical instruments and these skills require a great amount of time and effort to acquire. Researchers have been introducing haptic feedback systems in order to facilitate the process of learning motor skills but little research has expanded the possibility of applying to the field of musical instruments. Hence, we developed a system called "MoveMe" that provides three-dimensional haptic support for playing a musical instrument. The system guides a user's hands as if someone else was holding their hands to help a beginner play a musical instrument. With the system, an expert can pre-record his/her movements so that a beginner can play it back later as necessary. Alternatively, the system connects an expert and a beginner via two haptic robots and the expert can, in real time, guide and correct the beginner's movement. In addition to those functionalities, we introduce a new proficiency metric provided by force feedback. A master can evaluate how much a beginner has improved using both audio feedback as well as this new force-based metric. Through the experiments that we conducted, we found that our system is effective in terms of playing a song at a correct speed and rhythm.
''', 
    tags = [haptic, music_edu], 
)

vibro_tactile_drum = Paper(
    apa = r'''Tom, A., Singh, A., Daigle, M., Marandola, F., & Wanderley, M. (2020). Haptic Tutor-A haptics-based music education tool for beginners. In International Workshop on Haptic and Audio Interaction Design.''', 
    bib = r'''@inproceedings{tom2020haptic,
  title={Haptic Tutor-A haptics-based music education tool for beginners},
  author={Tom, Ajin and Singh, Ankita and Daigle, Martin and Marandola, Fabrice and Wanderley, Marcelo},
  booktitle={International Workshop on Haptic and Audio Interaction Design},
  year={2020}
}
''', 
    abstract = r'''In this paper we introduce Haptic Tutor, a wearable haptic system for triggering vibrations on limbs of a student drummer aimed to help develop multi-limb independence. The system uses portable, wireless vibrotactile devices to display haptic information on drummers' limbs. To asses the usefulness of the system, we analyse response time differences between stimuli and motor action (drum stroke). Our hypotheses are that the use of haptic stimuli will improve the temporal characteristics of performances, but also that the type of haptic stimuli will have an influence on performance results. To validate these hypotheses we conducted two experiments. The first one with participants randomly distributed in three groups, each group performing simple drumming lessons involving both hands under a given condition (no haptics, haptic pulse and haptic ramp). Results show clear improvement in strike accuracy for both haptic conditions, most clearly in the haptic ramp condition. Using these results, a second experiment was carried out in which 6 other participants were randomly divided into two groups (no haptics and haptic ramp conditions) and asked to perform a more complex lesson, this time involving three limbs (two arms and right foot). Results of both experiments show clear improvement on strike accuracy (reduced asynchrony), but a less important difference on strike precision (inter-onset-interval deviation) for the haptic condition. We finally report on participants subjective comments , discussing the limitations of the current prototype.''', 
    tags = [haptic, music_edu, vibration], 
)

scaffolding = Paper(
    apa = r'''Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. Journal of child psychology and psychiatry, 17(2), 89-100.''', 
    bib = r'''@article{wood1976role,
  title={The role of tutoring in problem solving},
  author={Wood, David and Bruner, Jerome S and Ross, Gail},
  journal={Journal of child psychology and psychiatry},
  volume={17},
  number={2},
  pages={89--100},
  year={1976},
  publisher={Wiley Online Library}
}
''', 
    abstract = None, 
    tags = [adaptive_curriculum_scaffolding], 
    my_notes = r'''
This paper proposed "scaffolding". 
scaffolding: focus on what little you can learn at the moment and leave the unlearnable to the tutor's assistance. 
I think: learn one thing at a time. 
''', 
)

fading_scaffold = Paper(
    apa = r'''McNeill, K. L., Lizotte, D. J., Krajcik, J., & Marx, R. W. (2006). Supporting students' construction of scientific explanations by fading scaffolds in instructional materials. The Journal of the Learning Sciences, 15(2), 153-191.''', 
    bib = r'''@article{mcneill2006supporting,
  title={Supporting students' construction of scientific explanations by fading scaffolds in instructional materials},
  author={McNeill, Katherine L and Lizotte, David J and Krajcik, Joseph and Marx, Ronald W},
  journal={The Journal of the Learning Sciences},
  volume={15},
  number={2},
  pages={153--191},
  year={2006},
  publisher={Taylor \& Francis}
}
''', 
    abstract = r'''The purpose of this study was to determine whether providing students with continuous written instructional support or fading written instructional support (scaffolds) better prepares students to construct scientific explanations when they are no longer provided with support. This article investigated the influence of scaffolding on 331 seventh-grade students' writing of scientific explanations during an 8-week, project-based chemistry unit in which the construction of scientific explanations is a key learning goal. The unit makes an instructional model for explanation explicit to students through a focal lesson and reinforces that model through subsequent written support for each investigation. Students received 1 of 2 treatments in terms of the type of written support: continuous, involving detailed support for every investigation, or faded, involving less support over time. The analyses showed significant learning gains for students for all components of scientific explanation (i.e., claim, evidence, and reasoning). However, on posttest items lacking scaffolds, the faded group gave stronger explanations in terms of their reasoning compared to the continuous group. Fading written scaffolds better equipped students to write explanations when they were not provided with support.''', 
    tags = [adaptive_curriculum_scaffolding], 
    my_notes = r'''fading scaffold''', 
)

xcp = Paper(
    apa = r'''Katabi, D., Handley, M., & Rohrs, C. (2002, August). Congestion control for high bandwidth-delay product networks. In Proceedings of the 2002 conference on Applications, technologies, architectures, and protocols for computer communications (pp. 89-102).''', 
    bib = r'''@inproceedings{katabi2002congestion,
  title={Congestion control for high bandwidth-delay product networks},
  author={Katabi, Dina and Handley, Mark and Rohrs, Charlie},
  booktitle={Proceedings of the 2002 conference on Applications, technologies, architectures, and protocols for computer communications},
  pages={89--102},
  year={2002}
}
''', 
    abstract = r'''Theory and experiments show that as the per-flow product of bandwidth and latency increases, TCP becomes inefficient and prone to instability, regardless of the queuing scheme. This failing becomes increasingly important as the Internet evolves to incorporate very high-bandwidth optical links and more large-delay satellite links.To address this problem, we develop a novel approach to Internet congestion control that outperforms TCP in conventional environments, and remains efficient, fair, scalable, and stable as the bandwidth-delay product increases. This new eXplicit Control Protocol, XCP, generalizes the Explicit Congestion Notification proposal (ECN). In addition, XCP introduces the new concept of decoupling utilization control from fairness control. This allows a more flexible and analytically tractable protocol design and opens new avenues for service differentiation.Using a control theory framework, we model XCP and demonstrate it is stable and efficient regardless of the link capacity, the round trip delay, and the number of sources. Extensive packet-level simulations show that XCP outperforms TCP in both conventional and high bandwidth-delay environments. Further, XCP achieves fair bandwidth allocation, high utilization, small standing queue size, and near-zero packet drops, with both steady and highly varying traffic. Additionally, the new protocol does not maintain any per-flow state in routers and requires few CPU cycles per packet, which makes it implementable in high-speed routers.''', 
    tags = [network], 
    my_notes = r'''
The router knows both the spare bandwidth and the queue. 
    THe routers mark the packets. 
Uses control theory to ensure stablity. 
''', 
)

deep_emb_helps_segmentation = Paper(
    apa = r'''Salamon, J., Nieto, O., & Bryan, N. J. (2017). Deep Embeddings and Section Fusion Improve Music Segmentation. IEEE Signal Processing Letters, 24(3), 279-283.''', 
    bib = r'''@article{salamon2017deep,
  title={Deep Embeddings and Section Fusion Improve Music Segmentation},
  author={Salamon, Justin and Nieto, Oriol and Bryan, Nicholas J},
  journal={IEEE Signal Processing Letters},
  volume={24},
  number={3},
  pages={279--283},
  year={2017}
}
''', 
    abstract = r'''Music segmentation algorithms identify the structure of a music recording by automatically dividing it into sections and determining which sections repeat and when. Since the desired granularity of the sections may vary by application, multi-level segmentation produces several levels of segmentation ordered by granularity from one section (the whole song) up to N unique sections, and has proven to be a challenging MIR task. In this work we propose a multi-level segmentation method that leverages deep audio embeddings learned via other tasks. Our approach builds on an existing multi-level segmentation algorithm, replacing manually engineered features with deep embeddings learned through audio classification problems where data are abundant. Additionally, we propose a novel section fusion algorithm that leverages the multi-level segmentation to consolidate short segments at each level in a way that is consistent with the segmentations at lower levels. Through a series of experiments we show that replacing handcrafted features with deep embeddings can lead to significant improvements in multilevel music segmentation performance, and that section fusion further improves the results by cleaning up spurious short sections. We compare our approach to two strong baselines and show that it yields state-of-the-art results.''', 
    tags = [hierarchical, time_hierarchy], 
    my_notes = r'''See slides at https://docs.google.com/presentation/d/143vXGAh7HiYN-WrxxkjLaHpi0NWK_2Md/edit?usp=sharing&ouid=111628173406875267677&rtpof=true&sd=true
Using deep emb to segmentate audio. 
No finetuning. Using existing clustering algo on deep emb. 
''', 
)

implementing_a_generative_theory_of_tonal_music = Paper(
    apa = r'''Hamanaka, M., Hirata, K., & Tojo, S. (2006). Implementing “A generative theory of tonal music”. Journal of New Music Research, 35(4), 249-277.''', 
    bib = r'''@article{hamanaka2006implementing,
  title={Implementing “A generative theory of tonal music”},
  author={Hamanaka, Masatoshi and Hirata, Keiji and Tojo, Satoshi},
  journal={Journal of New Music Research},
  volume={35},
  number={4},
  pages={249--277},
  year={2006},
  publisher={Taylor \& Francis}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Mechanize GTTM into exGTTM.  
ATTA is a rule-based algo to propose analysis under exGTTM.  
ATTA = automatic time-span tree analyser.  
It has 46 human-tuned parameters to specify the strength 
of different preference rules.  
It beats a baseline.  
ATTA is at http://
staff.aist.go.jp/m.hamanaka/atta/  
    input is musicXML.  
    Can be baseline? However, the human-tuned parameters 
    probably made it overfit. (not fully automatic) Also 
    it is monophonic.  
''', 
)

deepGTTM_I_II_local_boundary_and_metrical_structure_analyzer_based_on_deep_learning = Paper(
    apa = r'''Hamanaka, M., Hirata, K., & Tojo, S. (2016, July). deepGTTM-I&II: Local boundary and metrical structure analyzer based on deep learning technique. In International Symposium on Computer Music Multidisciplinary Research (pp. 3-21). Springer, Cham.''', 
    bib = r'''@inproceedings{hamanaka2016deepgttm,
  title={deepGTTM-I\&II: Local boundary and metrical structure analyzer based on deep learning technique},
  author={Hamanaka, Masatoshi and Hirata, Keiji and Tojo, Satoshi},
  booktitle={International Symposium on Computer Music Multidisciplinary Research},
  pages={3--21},
  year={2016},
  organization={Springer}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
8-bar monophonic.  
The output of the NN is not only the metrical structure, 
but also the applicability of GTTM rules on each note.  
The input has manually annotated grouping structure.  
    not sure. maybe a part of curriculum.  
NN is many FC layers.  
Misc. 
    Related work "FATTA" [3] can be baseline, but monophonic.  
''', 
)

music_structural_analysis_database_based_on_GTTM = Paper(
    apa = r'''Hamanaka, M., Hirata, K., & Tojo, S. (2014). Musical structural analysis database based on GTTM.''', 
    bib = r'''@article{hamanaka2014musical,
  title={Musical structural analysis database based on GTTM},
  author={Hamanaka, Masatoshi and Hirata, Keiji and Tojo, Satoshi},
  year={2014},
  publisher={ISMIR 2014}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022, dataset], 
    my_notes = r'''
A dataset of GTTM-annotated monophonic pieces, each ~ 8 bars.  
''', 
)

deepGTTM_III_simultaneous_learning_of_grouping_and_metrical_structures = Paper(
    apa = r'''Hirata, M. H. K., & Tojo, S. deepGTTM-III: Simultaneous Learning of Grouping and Metrical Structures.''', 
    bib = r'''@article{hiratadeepgttm,
  title={deepGTTM-III: Simultaneous Learning of Grouping and Metrical Structures},
  author={Hirata, Masatoshi Hamanaka1 Keiji and Tojo, Satoshi}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Include feedback between metrical and grouping structures.  
In practice, it's just multi-task learning using shared 
backbones.  
''', 
)

searching_for_metric_structure_of_musical_files = Paper(
    apa = r'''Kostek, B., Wojcik, J., & Szczuko, P. (2007, June). Searching for Metric Structure of Musical Files. In International Conference on Rough Sets and Intelligent Systems Paradigms (pp. 774-783). Springer, Berlin, Heidelberg.''', 
    bib = r'''@inproceedings{kostek2007searching,
  title={Searching for Metric Structure of Musical Files},
  author={Kostek, Bozena and Wojcik, Jaroslaw and Szczuko, Piotr},
  booktitle={International Conference on Rough Sets and Intelligent Systems Paradigms},
  pages={774--783},
  year={2007},
  organization={Springer}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Symbolic polyphonic -> ANN -> note accented or not.  
Only one level of metrical struct.  
''', 
)

machine_rhythm_computer_emulation_of_human_rhythm_perception = Paper(
    apa = r'''Rosenthal, D. F. (1992). Machine rhythm--computer emulation of human rhythm perception (Doctoral dissertation, Massachusetts Institute of Technology).''', 
    bib = r'''@phdthesis{rosenthal1992machine,
  title={Machine rhythm--computer emulation of human rhythm perception},
  author={Rosenthal, David Felix},
  year={1992},
  school={Massachusetts Institute of Technology}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Symbolic polyphonic -> "Machine Rhythm" 
-> 3-level rhythmic annotation  
A 1977 PhD thesis. So probably you can't get their code.  
''', 
)

modeling_meter_and_harmony_a_preference_rule_approach = Paper(
    apa = r'''Temperley, D., & Sleator, D. (1999). Modeling meter and harmony: A preference-rule approach. Computer Music Journal, 23(1), 10-27.''', 
    bib = r'''@article{temperley1999modeling,
  title={Modeling meter and harmony: A preference-rule approach},
  author={Temperley, David and Sleator, Daniel},
  journal={Computer Music Journal},
  volume={23},
  number={1},
  pages={10--27},
  year={1999},
  publisher={JSTOR}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Recommended reading.  
Symbolic polyphonic -> (
    5-level metrical struct + harmonic struct
)  
tactus is at level 2 (middle) among levels 0 : 5.  
Rule based.  
    pref rules: variations of GTTM.  
    Search: Dynamic programming.  
Open source at http://www.link.cs.cmu.edu/music-analysis  
    also includes their test set.  
    Probably, the test set is unlabeled and they did 
    subjective evaluations.  
''', 
)

inferring_metrical_structure_in_music_using_particle_filters = Paper(
    apa = r'''Krebs, F., Holzapfel, A., Cemgil, A. T., & Widmer, G. (2015). Inferring metrical structure in music using particle filters. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 23(5), 817-827.''', 
    bib = r'''@article{krebs2015inferring,
  title={Inferring metrical structure in music using particle filters},
  author={Krebs, Florian and Holzapfel, Andre and Cemgil, Ali Taylan and Widmer, Gerhard},
  journal={IEEE/ACM Transactions on Audio, Speech, and Language Processing},
  volume={23},
  number={5},
  pages={817--827},
  year={2015},
  publisher={IEEE}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
non symbolic -> 2-level metrical struct
''', 
)

gtsim_a_computer_simulation_of_music_perception = Paper(
    apa = r'''Jones, J., Scarborough, D., & Miller, B. (1993). Gtsim a computer simulation of music perception. Computers and the Humanities, 27(1), 19-23.''', 
    bib = r'''@article{jones1993gtsim,
  title={Gtsim a computer simulation of music perception},
  author={Jones, Jacqueline and Scarborough, Don and Miller, Benjamin},
  journal={Computers and the Humanities},
  volume={27},
  number={1},
  pages={19--23},
  year={1993},
  publisher={Springer}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Work in progress from 1993...  
''', 
)

on_hierarchical_clustering_of_spectrogram = Paper(
    apa = r'''Sawada, S., Takegawa, Y., & Hirata, K. (2017, September). On Hierarchical Clustering of Spectrogram. In International Symposium on Computer Music Multidisciplinary Research (pp. 226-237). Springer, Cham.''', 
    bib = r'''@inproceedings{sawada2017hierarchical,
  title={On Hierarchical Clustering of Spectrogram},
  author={Sawada, Shun and Takegawa, Yoshinari and Hirata, Keiji},
  booktitle={International Symposium on Computer Music Multidisciplinary Research},
  pages={226--237},
  year={2017},
  organization={Springer}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
spectrogram -> grouping struct  
Looks like a good paper, but so hard to read.  
没读完.  
''', 
)

a_constraint_based_approach_to_grouping_in_language_and_music = Paper(
    apa = r'''van der Werf, S., & Hendriks, P. (2004). A constraint-based approach to grouping in language and music. In Proceedings: First Conference on Interdisciplinary Musicology CIM04, Graz, Austria.''', 
    bib = r'''@inproceedings{van2004constraint,
  title={A constraint-based approach to grouping in language and music},
  author={van der Werf, Sybrand and Hendriks, Petra},
  booktitle={Proceedings: First Conference on Interdisciplinary Musicology CIM04, Graz, Austria},
  year={2004}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
GTTM -> OT (optimality theory).  
Gives a parser for symbolic monophonic short pieces.  
Compares with human annotations.  
Parser is based on the magic of Prolog.  
''', 
)

a_rule_based_expert_system_for_music_perception = Paper(
    apa = r'''Jones, J. A., Miller, B. O., & Scarborough, D. L. (1988). A rule-based expert system for music perception. Behavior Research Methods, Instruments, & Computers, 20(2), 255-262.''', 
    bib = r'''@article{jones1988rule,
  title={A rule-based expert system for music perception},
  author={Jones, Jacqueline A and Miller, Benjamin O and Scarborough, Don L},
  journal={Behavior Research Methods, Instruments, \& Computers},
  volume={20},
  number={2},
  pages={255--262},
  year={1988},
  publisher={Springer}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
monophonic symbolic -> 6-level metrical struct  
1988 的在读 PhD 搞的， 估计要不来 source code.  
Rule-based. Does not *seem* to consider PR, only WFR.  
''', 
)

a_theoretical_framework_for_rhythm_perception = Paper(
    apa = r'''Povel, D. J. (1984). A theoretical framework for rhythm perception. Psychological research, 45(4), 315-337.''', 
    bib = r'''@article{povel1984theoretical,
  title={A theoretical framework for rhythm perception},
  author={Povel, Dirk-Jan},
  journal={Psychological research},
  volume={45},
  number={4},
  pages={315--337},
  year={1984},
  publisher={Springer}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Proposes grid theory.  
"Pre-GTTM" simple theory to parse simple rhythm.  
''', 
)

perception_of_temporal_patterns = Paper(
    apa = r'''Povel, D. J., & Essens, P. (1985). Perception of temporal patterns. Music perception, 2(4), 411-440.''', 
    bib = r'''@article{povel1985perception,
  title={Perception of temporal patterns},
  author={Povel, Dirk-Jan and Essens, Peter},
  journal={Music perception},
  volume={2},
  number={4},
  pages={411--440},
  year={1985},
  publisher={University of California Press}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Another non-GTTM rhythm perception theory.  
It's more or less a 2-level struct.  
Proposes an algo too.  
''', 
)

a_review_of_automatic_rhythm_description_systems = Paper(
    apa = r'''Gouyon, F., & Dixon, S. (2005). A review of automatic rhythm description systems. Computer music journal, 29(1), 34-54.''', 
    bib = r'''@article{gouyon2005review,
  title={A review of automatic rhythm description systems},
  author={Gouyon, Fabien and Dixon, Simon},
  journal={Computer music journal},
  volume={29},
  number={1},
  pages={34--54},
  year={2005},
  publisher={JSTOR}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
A lit review of many rhythm trackers.  
Notes the commonality of their methods.  
However, seems to emphasize only levels 0:3.  
Also input is non-symbolic audio.  
Section "Time Signature Determination" is useful.  
''', 
)

a_hybrid_graphical_model_for_rhythmic_parsing = Paper(
    apa = r'''Raphael, C. (2002). A hybrid graphical model for rhythmic parsing. Artificial Intelligence, 137(1-2), 217-238.''', 
    bib = r'''@article{raphael2002hybrid,
  title={A hybrid graphical model for rhythmic parsing},
  author={Raphael, Christopher},
  journal={Artificial Intelligence},
  volume={137},
  number={1-2},
  pages={217--238},
  year={2002},
  publisher={Elsevier}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
symbolic -> rhythm parse  
method: ???  
''', 
)

robust_downbeat_tracking_using_an_ensemble_of_convolutional_networks = Paper(
    apa = r'''Durand, S., Bello, J. P., David, B., & Richard, G. (2016). Robust downbeat tracking using an ensemble of convolutional networks. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 25(1), 76-89.''', 
    bib = r'''@article{durand2016robust,
  title={Robust downbeat tracking using an ensemble of convolutional networks},
  author={Durand, Simon and Bello, Juan Pablo and David, Bertrand and Richard, Ga{\"e}l},
  journal={IEEE/ACM Transactions on Audio, Speech, and Language Processing},
  volume={25},
  number={1},
  pages={76--89},
  year={2016},
  publisher={IEEE}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
)

a_generalized_bayesian_model_for_tracking_long_metrical_cycles_in_acoustic_music_signals = Paper(
    apa = r'''Srinivasamurthy, A., Holzapfel, A., Cemgil, A. T., & Serra, X. (2016, March). A generalized bayesian model for tracking long metrical cycles in acoustic music signals. In 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 76-80). IEEE.''', 
    bib = r'''@inproceedings{srinivasamurthy2016generalized,
  title={A generalized bayesian model for tracking long metrical cycles in acoustic music signals},
  author={Srinivasamurthy, Ajay and Holzapfel, Andre and Cemgil, Ali Taylan and Serra, Xavier},
  booktitle={2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={76--80},
  year={2016},
  organization={IEEE}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Meter tracking improved for non-western music where each bar 
is very long.  
''', 
)

automatic_salience_based_hypermetric_rhythm_retrieval = Paper(
    apa = r'''Kostek, B., & Wojcik, J. (2007, April). Automatic salience-based hypermetric rhythm retrieval. In 2007 International Conference on Multimedia and Ubiquitous Engineering (MUE'07) (pp. 1220-1226). IEEE.''', 
    bib = r'''@inproceedings{kostek2007automatic,
  title={Automatic salience-based hypermetric rhythm retrieval},
  author={Kostek, Bozena and Wojcik, Jaroslaw},
  booktitle={2007 International Conference on Multimedia and Ubiquitous Engineering (MUE'07)},
  pages={1220--1226},
  year={2007},
  organization={IEEE}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
整篇一直在说 hypermetric rhythm, 但整篇没看到。  
''', 
)

a_unified_probabilistic_model_for_polyphonic_music_analysis = Paper(
    apa = r'''Temperley, D. (2009). A unified probabilistic model for polyphonic music analysis. Journal of New Music Research, 38(1), 3-18.''', 
    bib = r'''@article{temperley2009unified,
  title={A unified probabilistic model for polyphonic music analysis},
  author={Temperley, David},
  journal={Journal of New Music Research},
  volume={38},
  number={1},
  pages={3--18},
  year={2009},
  publisher={Taylor \& Francis}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
polyphonic symbolic -> metrical + harmonic + stream struct  
Open source at http://www.theory.esm.rochester/  
Generative -- Bayesian -> analytical  
The metrical rules are more strict than GTTM, only giving 
very regular parses.  
''', 
)

determination_of_the_meter_of_musical_scores_by_autocorrelation = Paper(
    apa = r'''Brown, J. C. (1993). Determination of the meter of musical scores by autocorrelation. The Journal of the Acoustical Society of America, 94(4), 1953-1957.''', 
    bib = r'''@article{brown1993determination,
  title={Determination of the meter of musical scores by autocorrelation},
  author={Brown, Judith C},
  journal={The Journal of the Acoustical Society of America},
  volume={94},
  number={4},
  pages={1953--1957},
  year={1993},
  publisher={Acoustical Society of America}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Assumes more notes are at downbeats than at upbeats.  
Trivially, autocorrelation can expose the meter.  
No pitch, only onsets.  
''', 
)

automatic_meter_extraction_from_midi_files = Paper(
    apa = r'''Meudic, B. (2002, June). Automatic meter extraction from MIDI files. In Journées d'informatique musicale (pp. 1-1).''', 
    bib = r'''@inproceedings{meudic2002automatic,
  title={Automatic meter extraction from MIDI files},
  author={Meudic, Benoit},
  booktitle={Journ{\'e}es d'informatique musicale},
  pages={1--1},
  year={2002}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
symbolic polyphonic -> 4-level metrical struct  
No link to source code. Ask authors.  
The main goal is to infer the meter.  
Method is auto-correlation.  
''', 
)

finding_meter_in_music_using_an_autocorrelation_phase_matrix_and_shannon_entropy = Paper(
    apa = r'''Eck, D., & Casagrande, N. (2005). Finding meter in music using an autocorrelation phase matrix and shannon entropy. Target, 300(350), 400.''', 
    bib = r'''@article{eck2005finding,
  title={Finding meter in music using an autocorrelation phase matrix and shannon entropy},
  author={Eck, Douglas and Casagrande, Norman},
  journal={Target},
  volume={300},
  number={350},
  pages={400},
  year={2005}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
)

meter_detection_in_symbolic_music_using_inner_metric_analysis = Paper(
    apa = r'''De Haas, W. B., & Volk, A. (2016, August). Meter detection in symbolic music using inner metric analysis. In International Society for Music Information Retrieval Conference (p. 441).''', 
    bib = r'''@inproceedings{de2016meter,
  title={Meter detection in symbolic music using inner metric analysis},
  author={De Haas, W Bas and Volk, Anja},
  booktitle={International Society for Music Information Retrieval Conference},
  pages={441},
  year={2016}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
)

automatic_generation_of_grouping_structure_based_on_the_gttm = Paper(
    apa = r'''Hamanaka, M., Hirata, K., & Tojo, S. (2004, November). Automatic Generation of Grouping Structure based on the GTTM. In ICMC.''', 
    bib = r'''@inproceedings{hamanaka2004automatic,
  title={Automatic Generation of Grouping Structure based on the GTTM},
  author={Hamanaka, Masatoshi and Hirata, Keiji and Tojo, Satoshi},
  booktitle={ICMC},
  year={2004}
}''', 
    abstract = None, 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Looks just like ATTA.  
''', 
)

beat_and_downbeat_tracking_of_symbolic_music_data_using_deep_recurrent_neural_networks = Paper(
    apa = r'''Chuang, Y. C., & Su, L. (2020, December). Beat and downbeat tracking of symbolic music data using deep recurrent neural networks. In 2020 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC) (pp. 346-352). IEEE.''', 
    bib = r'''@inproceedings{chuang2020beat,
  title={Beat and downbeat tracking of symbolic music data using deep recurrent neural networks},
  author={Chuang, Yi-Chin and Su, Li},
  booktitle={2020 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC)},
  pages={346--352},
  year={2020},
  organization={IEEE}
}''', 
    abstract = r'''Musical beat tracking is one of the most investigated tasks in music information retrieval (MIR). Research endeavors on this task have mostly been focused on the modeling of audio data representations. In contrast, beat tracking of symbolic music contents (e.g., MIDI, score sheets) has been relatively overlooked in the past years. In this paper, we revisit the task of symbolic music beat tracking and present to solve this task with modern deep learning approaches. To the extent of our knowledge, it is the first time that utilizing deep learning approaches to track beats and downbeats of symbolic music data. The proposed symbolic beat tracking framework performs joint beat and downbeat tracking in a multi-task learning (MTL) manner, and we investigate various types of networks which are based on the recurrent neural networks (RNN), such as bidirectional long short-term memory (BLSTM) network, hierarchical multi-scale (HM) LSTM, and BLSTM with the attention mechanism. In the experiments, a systematic comparison of these networks and state-of-art audio beat tracking methods are performed on the MusicNet dataset. Experiment results show that the BLSTM model trained specifically on symbolic data outperforms the state-of-the-art beat tracking methods utilized on synthesized audio. Such a comparison of performance also indicates the technical challenges in symbolic music beat tracking.''', 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Double binary classification (beat? downbeat?) for each 
timestep.  
''', 
)

representations_of_music_in_ranking_rhythmic_hypotheses = Paper(
    apa = r'''Wojcik, J., & Kostek, B. (2010). Representations of music in ranking rhythmic hypotheses. In Advances in Music Information Retrieval (pp. 39-64). Springer, Berlin, Heidelberg.''', 
    bib = r'''@incollection{wojcik2010representations,
  title={Representations of music in ranking rhythmic hypotheses},
  author={Wojcik, Jaroslaw and Kostek, Bozena},
  booktitle={Advances in Music Information Retrieval},
  pages={39--64},
  year={2010},
  publisher={Springer}
}''', 
    abstract = r'''The chapter presents first the main issues related to music information retrieval (MIR) domain. Within this domain, there exists a variety of approaches to musical instrument recognition, musical phrase classification, melody classification (e.g. query-by-humming systems), rhythm retrieval, retrieval of high-level-musical features such as looking for emotions in music or differences in expressiveness, music search based on listeners’ preferences, etc. The objective of this study is to propose a method for retrieval of hypermetric rhythm on the basis of melody. A stream of sounds in MIDI format is introduced at the system input. On the basis of a musical content the method retrieves a hypermetric structure of rhythm of a musical piece consisting of rhythmic motives, phrases, and sentences. On the basis of the hypermetric structure retrieved, a system capable of creating automatic drum accompaniment to a given melody supporting the composition is proposed. A method does not use any information about rhythm (time signature), which is often included in MIDI information. Neither rhythmic tracks nor harmonic information are used in this method. The only information analyzed is a melody, which may be monophonic as well as polyphonic. The analysis starts after the entire piece has been played. Recurrence of melodic and rhythmic patterns and the rhythmic salience of sounds are combined to create an algorithm that finds the metric structure of rhythm in a given melody.''', 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Actually hypermeter parsing.  
"The objective of this study is to propose a method for 
retrieval of hypermetric rhythm on the basis of melody"  
Propose parses and rank them using rule-based.  
''', 
)

enhanced_hierarchical_music_structure_annotations_via_feature_level_similarity_fusion = Paper(
    apa = r'''Tralie, C. J., & McFee, B. (2019, May). Enhanced hierarchical music structure annotations via feature level similarity fusion. In ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 201-205). IEEE.''', 
    bib = r'''@inproceedings{tralie2019enhanced,
  title={Enhanced hierarchical music structure annotations via feature level similarity fusion},
  author={Tralie, Christopher J and McFee, Brian},
  booktitle={ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={201--205},
  year={2019},
  organization={IEEE}
}''', 
    abstract = r'''We describe a novel pipeline to automatically discover hierarchies of repeated sections in musical audio. The proposed method uses similarity network fusion (SNF) to combine different frame-level features into clean affinity matrices, which are then used as input to spectral clustering. While prior spectral clustering approaches to music structure analysis have pre-processed affinity matrices with heuristics specifically designed for this task, we show that the SNF approach directly yields segmentations which agree better with human annotators, as measured by the "L-measure" metric for hierarchical annotations. Furthermore, the SNF approach immediately supports arbitrarily many input features, allowing us to simultaneously discover structure encoded in timbral, harmonic, and rhythmic representations without any changes to the base algorithm.''', 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
SNF (similarity network fusion) can fuse multiple similarity 
metrics. Then, they use spectral clustering.  
''', 
)

unsupervised_music_structure_annotation_by_time_series_structure_features_and_segment_similarity = Paper(
    apa = r'''Serra, J., Müller, M., Grosche, P., & Arcos, J. L. (2014). Unsupervised music structure annotation by time series structure features and segment similarity. IEEE Transactions on Multimedia, 16(5), 1229-1240.''', 
    bib = r'''@article{serra2014unsupervised,
  title={Unsupervised music structure annotation by time series structure features and segment similarity},
  author={Serra, Joan and M{\"u}ller, Meinard and Grosche, Peter and Arcos, Josep Ll},
  journal={IEEE Transactions on Multimedia},
  volume={16},
  number={5},
  pages={1229--1240},
  year={2014},
  publisher={IEEE}
}''', 
    abstract = r'''Automatically inferring the structural properties of raw multimedia documents is essential in today's digitized society. Given its hierarchical and multi-faceted organization, musical pieces represent a challenge for current computational systems. In this article, we present a novel approach to music structure annotation based on the combination of structure features with time series similarity. Structure features encapsulate both local and global properties of a time series, and allow us to detect boundaries between homogeneous, novel, or repeated segments. Time series similarity is used to identify equivalent segments, corresponding to musically meaningful parts. Extensive tests with a total of five benchmark music collections and seven different human annotations show that the proposed approach is robust to different ground truth choices and parameter settings. Moreover, we see that it outperforms previous approaches evaluated under the same framework.''', 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
Intro has a nice review.  
Not only clustering, but also cut according to novelty peaks.  
我没读完。  
''', 
)

boundary_detection_in_music_structure_analysis_using_convolutional_neural_networks = Paper(
    apa = r'''Ullrich, K., Schlüter, J., & Grill, T. (2014, October). Boundary Detection in Music Structure Analysis using Convolutional Neural Networks. In ISMIR (pp. 417-422).''', 
    bib = r'''@inproceedings{ullrich2014boundary,
  title={Boundary Detection in Music Structure Analysis using Convolutional Neural Networks.},
  author={Ullrich, Karen and Schl{\"u}ter, Jan and Grill, Thomas},
  booktitle={ISMIR},
  pages={417--422},
  year={2014}
}''', 
    abstract = r'''The recognition of boundaries, e.g., between chorus andverse, is an important task in music structure analysis. Thegoal is to automatically detect such boundaries in audiosignals so that the results are close to human annotation.In this work, we apply Convolutional Neural Networks tothe task, trained directly on mel-scaled magnitude spectrograms. On a representative subset of the SALAMI structural annotation dataset, our method outperforms currenttechniques in terms of boundary retrieval F-measure at different temporal tolerances: We advance the state-of-the-artfrom 0.33 to 0.46 for tolerances of ±0.5 seconds, and from0.52 to 0.62 for tolerances of ±3 seconds. As the algorithm is trained on annotated audio data without the needof expert knowledge, we expect it to be easily adaptableto changed annotation guidelines and also to related taskssuch as the detection of song transitions.''', 
    tags = [lit_review_for_junyan_ismir_2022], 
)

automatic_analysis_and_influence_of_hierarchical_structure_on_melody_rhythm_and_harmony_in_popular_music = Paper(
    apa = r'''Dai, S., Zhang, H., & Dannenberg, R. B. (2020). Automatic analysis and influence of hierarchical structure on melody, rhythm and harmony in popular music. arXiv preprint arXiv:2010.07518.''', 
    bib = r'''@article{dai2020automatic,
  title={Automatic analysis and influence of hierarchical structure on melody, rhythm and harmony in popular music},
  author={Dai, Shuqi and Zhang, Huan and Dannenberg, Roger B},
  journal={arXiv preprint arXiv:2010.07518},
  year={2020}
}''', 
    abstract = r'''Repetition is a basic indicator of musical structure. This study introduces new algorithms for identifying musical phrases based on repetition. Phrases combine to form sections yielding a two-level hierarchical structure. Automatically detected hierarchical repetition structures reveal significant interactions between structure and chord progressions, melody and rhythm. Different levels of hierarchy interact differently, providing evidence that structural hierarchy plays an important role in music beyond simple notions of repetition or similarity. Our work suggests new applications for music generation and music evaluation.''', 
    tags = [lit_review_for_junyan_ismir_2022], 
    my_notes = r'''
First segment the song by minimizing SDL (Structure 
Description Length).  
''', 
)

hierarchical_motion_understanding_via_motion_programs = Paper(
    apa = r'''Kulal, S., Mao, J., Aiken, A., & Wu, J. (2021). Hierarchical motion understanding via motion programs. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 6568-6576).''', 
    bib = r'''@inproceedings{kulal2021hierarchical,
  title={Hierarchical motion understanding via motion programs},
  author={Kulal, Sumith and Mao, Jiayuan and Aiken, Alex and Wu, Jiajun},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={6568--6576},
  year={2021}
}''', 
    abstract = r'''Current approaches to video analysis of human motion focus on raw pixels or keypoints as the basic units of reasoning. We posit that adding higher-level motion primitives, which can capture natural coarser units of motion such as backswing or follow-through, can be used to improve downstream analysis tasks. This higher level of abstraction can also capture key features, such as loops of repeated primitives, that are currently inaccessible at lower levels of representation. We therefore introduce Motion Programs, a neuro-symbolic, program-like representation that expresses motions as a composition of high-level primitives. We also present a system for automatically inducing motion programs from videos of human motion and for leveraging motion programs in video synthesis. Experiments show that motion programs can accurately describe a diverse set of human motions and the inferred programs contain semantically meaningful motion primitives, such as arm swings and jumping jacks. Our representation also benefits downstream tasks such as video interpolation and video prediction and outperforms off-the-shelf models. We further demonstrate how these programs can detect diverse kinds of repetitive motion and facilitate interactive video editing.''', 
    tags = [computer_vision], 
    my_notes = r'''
Just one level of time hierarchy. Simple inductive bias to understand human videos. Ablation tests are a little insufficient, I would say. 
''', 
)

overcoming_the_disentanglement_vs_reconstruction_trade_off_via_jacobian_supervision = Paper(
    apa = r'''Lezama, J. (2018, September). Overcoming the disentanglement vs reconstruction trade-off via Jacobian supervision. In International Conference on Learning Representations.''', 
    bib = r'''@inproceedings{lezama2018overcoming,
  title={Overcoming the disentanglement vs reconstruction trade-off via Jacobian supervision},
  author={Lezama, Jos{\'e}},
  booktitle={International Conference on Learning Representations},
  year={2018}
}''', 
    abstract = r'''A major challenge in learning image representations is the disentangling of the factors of variation underlying the image formation.  This is typically achieved with an autoencoder architecture where a subset of the latent variables is constrained to correspond to specific factors, and the rest of them are considered nuisance variables. This approach has an important drawback: as the dimension of the nuisance variables is increased, image reconstruction is improved, but the decoder has the flexibility to ignore the specified factors, thus losing the ability to condition the output on them.  In this work, we propose to overcome this trade-off by progressively growing the dimension of the latent code, while constraining the Jacobian of the output image with respect to the disentangled variables to remain the same.  As a result, the obtained models are effective at both disentangling and reconstruction.  We demonstrate the applicability of this method in both unsupervised and supervised scenarios for learning disentangled representations. In a facial attribute manipulation task, we obtain high quality image generation while smoothly controlling dozens of attributes with a single model. This is an order of magnitude more disentangled factors than state-of-the-art methods, while obtaining visually similar or superior results, and avoiding adversarial training.''', 
    tags = [], 
)

time_in_distributed_real_time_systems = Paper(
    apa = r'''Brandt, E., & Dannenberg, R. B. (1999). Time in distributed real-time systems.''', 
    bib = r'''@article{brandt1999time,
  title={Time in distributed real-time systems},
  author={Brandt, Eli and Dannenberg, Roger B},
  year={1999},
  publisher={Carnegie Mellon University}
}''', 
    abstract = r'''A real-time music system is responsible for deciding what happens when, when each task runs and each message takes effect. This question becomes acute when there are several classes of tasks running and intercommunicating: user interface, control processing, and audio, for example. We briefly examine and classify past approaches and their applicability to distributed systems, then propose and discuss an alternative. The shared access to a sample clock that it requires is not trivial to achieve in a distributed system, so we describe and assess a way to do so.''', 
    tags = [realtime], 
    my_notes = r'''
For ardu and proc, use midpoint estimate.  
''', 
)

make_a_video_text_to_video_generation_without_text_video_data = Paper(
    apa = r'''Singer, U., Polyak, A., Hayes, T., Yin, X., An, J., Zhang, S., ... & Taigman, Y. (2022). Make-A-Video: Text-to-Video Generation without Text-Video Data. arXiv preprint arXiv:2209.14792.''', 
    bib = r'''@article{singer2022make,
  title={Make-A-Video: Text-to-Video Generation without Text-Video Data},
  author={Singer, Uriel and Polyak, Adam and Hayes, Thomas and Yin, Xi and An, Jie and Zhang, Songyang and Hu, Qiyuan and Yang, Harry and Ashual, Oron and Gafni, Oran and others},
  journal={arXiv preprint arXiv:2209.14792},
  year={2022}
}''', 
    abstract = r'''We propose Make-A-Video -- an approach for directly translating the tremendous recent progress in Text-to-Image (T2I) generation to Text-to-Video (T2V). Our intuition is simple: learn what the world looks like and how it is described from paired text-image data, and learn how the world moves from unsupervised video footage. Make-A-Video has three advantages: (1) it accelerates training of the T2V model (it does not need to learn visual and multimodal representations from scratch), (2) it does not require paired text-video data, and (3) the generated videos inherit the vastness (diversity in aesthetic, fantastical depictions, etc.) of today's image generation models. We design a simple yet effective way to build on T2I models with novel and effective spatial-temporal modules. First, we decompose the full temporal U-Net and attention tensors and approximate them in space and time. Second, we design a spatial temporal pipeline to generate high resolution and frame rate videos with a video decoder, interpolation model and two super resolution models that can enable various applications besides T2V. In all aspects, spatial and temporal resolution, faithfulness to text, and quality, Make-A-Video sets the new state-of-the-art in text-to-video generation, as determined by both qualitative and quantitative measures.''', 
    tags = [diffusion], 
    my_notes = r'''
It's text to image (embedding) to video.  
The image 2 video part finetunes an existing image diffusion model.  i.e. the 3rd D is added and then trained.  
Various details and techniques are worth learning from.  
''', 
)

learning_temporally_causal_latent_processes_from_general_temporal_data = Paper(
    apa = r'''Yao, W., Sun, Y., Ho, A., Sun, C., & Zhang, K. (2021). Learning Temporally Causal Latent Processes from General Temporal Data. arXiv preprint arXiv:2110.05428.''', 
    bib = r'''@article{yao2021learning,
  title={Learning Temporally Causal Latent Processes from General Temporal Data},
  author={Yao, Weiran and Sun, Yuewen and Ho, Alex and Sun, Changyin and Zhang, Kun},
  journal={arXiv preprint arXiv:2110.05428},
  year={2021}
}''', 
    abstract = r'''Our goal is to recover time-delayed latent causal variables and identify their relations from measured temporal data. Estimating causally-related latent variables from observations is particularly challenging as the latent variables are not uniquely recoverable in the most general case. In this work, we consider both a nonparametric, nonstationary setting and a parametric setting for the latent processes and propose two provable conditions under which temporally causal latent processes can be identified from their nonlinear mixtures. We propose LEAP, a theoretically-grounded framework that extends Variational AutoEncoders (VAEs) by enforcing our conditions through proper constraints in causal process prior. Experimental results on various datasets demonstrate that temporally causal latent processes are reliably identified from observed variables under different dependency structures and that our approach considerably outperforms baselines that do not properly leverage history or nonstationarity information. This demonstrates that using temporal information to learn latent processes from their invertible nonlinear mixtures in an unsupervised manner, for which we believe our work is one of the first, seems promising even without sparsity or minimality assumptions.''', 
    tags = [causality, self_supervise, relation], 
    my_notes = r'''
"LEAP", "五小球".  
Using causality (高深，我不懂) to learn a system concepts from video.  
What I don't understand:  
why is it possible to infer causality when there's noise?  
Say x, \epsilon -> y. We observe x and y. How do we know the direction of the causation?  
''', 
)

the_surprising_effectiveness_of_equivariant_models_in_domains_with_latent_symmetry = Paper(
    apa = r'''Wang, D., Park, J. Y., Sortur, N., Wong, L. L., Walters, R., & Platt, R. (2022). The surprising effectiveness of equivariant models in domains with latent symmetry. arXiv preprint arXiv:2211.09231.''', 
    bib = r'''@article{wang2022surprising,
  title={The surprising effectiveness of equivariant models in domains with latent symmetry},
  author={Wang, Dian and Park, Jung Yeon and Sortur, Neel and Wong, Lawson LS and Walters, Robin and Platt, Robert},
  journal={arXiv preprint arXiv:2211.09231},
  year={2022}
}''', 
    abstract = r'''Extensive work has demonstrated that equivariant neural networks can significantly improve sample efficiency and generalization by enforcing an inductive bias in the network architecture. These applications typically assume that the domain symmetry is fully described by explicit transformations of the model inputs and outputs. However, many real-life applications contain only latent or partial symmetries which cannot be easily described by simple transformations of the input. In these cases, it is necessary to learn symmetry in the environment instead of imposing it mathematically on the network architecture. We discover, surprisingly, that imposing equivariance constraints that do not exactly match the domain symmetry is very helpful in learning the true symmetry in the environment. We differentiate between extrinsic and incorrect symmetry constraints and show that while imposing incorrect symmetry can impede the model's performance, imposing extrinsic symmetry can actually improve performance. We demonstrate that an equivariant model can significantly outperform non-equivariant methods on domains with latent symmetries both in supervised learning and in reinforcement learning for robotic manipulation and control problems.''', 
    tags = [symmetry], 
    my_notes = r'''
it seems that plain encoders with wrong symm can learn well.  
''', 
)

diffusion_lm_improves_controllable_text_generation = Paper(
    apa = r'''Li, X. L., Thickstun, J., Gulrajani, I., Liang, P., & Hashimoto, T. B. (2022). Diffusion-LM Improves Controllable Text Generation. arXiv preprint arXiv:2205.14217.''', 
    bib = r'''@article{li2022diffusion,
  title={Diffusion-LM Improves Controllable Text Generation},
  author={Li, Xiang Lisa and Thickstun, John and Gulrajani, Ishaan and Liang, Percy and Hashimoto, Tatsunori B},
  journal={arXiv preprint arXiv:2205.14217},
  year={2022}
}''', 
    abstract = r'''Controlling the behavior of language models (LMs) without re-training is a major open problem in natural language generation. While recent works have demonstrated successes on controlling simple sentence attributes (e.g., sentiment), there has been little progress on complex, fine-grained controls (e.g., syntactic structure). To address this challenge, we develop a new non-autoregressive language model based on continuous diffusions that we call Diffusion-LM. Building upon the recent successes of diffusion models in continuous domains, Diffusion-LM iteratively denoises a sequence of Gaussian vectors into word vectors, yielding a sequence of intermediate latent variables. The continuous, hierarchical nature of these intermediate variables enables a simple gradient-based algorithm to perform complex, controllable generation tasks. We demonstrate successful control of Diffusion-LM for six challenging fine-grained control tasks, significantly outperforming prior work.''', 
    tags = [diffusion, control, nlp], 
    my_notes = r'''
read abstract and Fig. 1.  
Fairly straight forward.  
Presented on study group: https://docs.google.com/presentation/d/1cuB6Y67DCRje5U3fvr08c2671iqo_4CG/edit?usp=share_link&ouid=111628173406875267677&rtpof=true&sd=true  

The condition is applied via classifier guidance.  
The classifier is trained to classify diffusion-intermediate vectors.  
During inference, alternate between classifier grad step and diffusion denoise step.  
''', 
)

exploiting_pre_trained_feature_networks_for_generative_adversarial_networks_in_audio_domain_loop_generation = Paper(
    apa = r'''Yeh, Y. T., Chen, B. Y., & Yang, Y. H. (2022). Exploiting Pre-trained Feature Networks for Generative Adversarial Networks in Audio-domain Loop Generation. arXiv preprint arXiv:2209.01751.''', 
    bib = r'''@article{yeh2022exploiting,
  title={Exploiting Pre-trained Feature Networks for Generative Adversarial Networks in Audio-domain Loop Generation},
  author={Yeh, Yen-Tung and Chen, Bo-Yu and Yang, Yi-Hsuan},
  journal={arXiv preprint arXiv:2209.01751},
  year={2022}
}''', 
    abstract = r'''While generative adversarial networks (GANs) have been widely used in research on audio generation, the training of a GAN model is known to be unstable, time consuming, and data inefficient. Among the attempts to ameliorate the training process of GANs, the idea of Projected GAN emerges as an effective solution for GAN-based image generation, establishing the state-of-the-art in different image applications. The core idea is to use a pre-trained classifier to constrain the feature space of the discriminator to stabilize and improve GAN training. This paper investigates whether Projected GAN can similarly improve audio generation, by evaluating the performance of a StyleGAN2-based audio-domain loop generation model with and without using a pre-trained feature space in the discriminator. Moreover, we compare the performance of using a general versus domain-specific classifier as the pre-trained audio classifier. With experiments on both drum loop and synth loop generation, we show that a general audio classifier works better, and that with Projected GAN our loop generation models can converge around 5 times faster without performance degradation.''', 
    tags = [ismir2022, gan], 
)

projected_gans_converge_faster = Paper(
    apa = r'''Sauer, A., Chitta, K., Müller, J., & Geiger, A. (2021). Projected gans converge faster. Advances in Neural Information Processing Systems, 34, 17480-17492.''', 
    bib = r'''@article{sauer2021projected,
  title={Projected gans converge faster},
  author={Sauer, Axel and Chitta, Kashyap and M{\"u}ller, Jens and Geiger, Andreas},
  journal={Advances in Neural Information Processing Systems},
  volume={34},
  pages={17480--17492},
  year={2021}
}''', 
    abstract = r'''Generative Adversarial Networks (GANs) produce high-quality images but are challenging to train. They need careful regularization, vast amounts of compute, and expensive hyper-parameter sweeps. We make significant headway on these issues by projecting generated and real samples into a fixed, pretrained feature space. Motivated by the finding that the discriminator cannot fully exploit features from deeper layers of the pretrained model, we propose a more effective strategy that mixes features across channels and resolutions. Our Projected GAN improves image quality, sample efficiency, and convergence speed. It is further compatible with resolutions of up to one Megapixel and advances the state-of-the-art Fréchet Inception Distance (FID) on twenty-two benchmark datasets. Importantly, Projected GANs match the previously lowest FIDs up to 40 times faster, cutting the wall-clock time from 5 days to less than 3 hours given the same computational resources.''', 
    tags = [gan], 
    my_notes = r'''
Uses random CCM and CSM to make discriminator look at the entire feature.  
Q1. Why is 1x1 conv not trivially invertible?  
    I wrote an email to ask the 1st author.  
Q2. Why does this method not suffer from vanishing gradients?  
''', 
)

equivariant_self_supervision_for_musical_tempo_estimation = Paper(
    apa = r'''Quinton, E. (2022). Equivariant Self-Supervision for Musical Tempo Estimation. arXiv preprint arXiv:2209.01478.''', 
    bib = r'''@article{quinton2022equivariant,
  title={Equivariant Self-Supervision for Musical Tempo Estimation},
  author={Quinton, Elio},
  journal={arXiv preprint arXiv:2209.01478},
  year={2022}
}''', 
    abstract = r'''Self-supervised methods have emerged as a promising avenue for representation learning in the recent years since they alleviate the need for labeled datasets, which are scarce and expensive to acquire. Contrastive methods are a popular choice for self-supervision in the audio domain, and typically provide a learning signal by forcing the model to be invariant to some transformations of the input. These methods, however, require measures such as negative sampling or some form of regularisation to be taken to prevent the model from collapsing on trivial solutions. In this work, instead of invariance, we propose to use equivariance as a self-supervision signal to learn audio tempo representations from unlabelled data. We derive a simple loss function that prevents the network from collapsing on a trivial solution during training, without requiring any form of regularisation or negative sampling. Our experiments show that it is possible to learn meaningful representations for tempo estimation by solely relying on equivariant self-supervision, achieving performance comparable with supervised methods on several benchmarks. As an added benefit, our method only requires moderate compute resources and therefore remains accessible to a wide research community.''', 
    tags = [ismir2022, self_supervise], 
    my_notes = r'''
SPICE, but extracts tempo.  
(Not exactly, because SPICE is still different.)  
''', 
)

semantic_control_of_generative_musical_attributes = Paper(
    apa = None, 
    bib = None, 
    abstract = r'''Deep generative neural networks have been successful in tasks such as composing novel music and rendering expressive performance. Controllability is essential for building creative tools from such models. Recent work in this area has focused on disentangled latent space representations, but this is only part of the solution. Efficient control of semantic attributes must handle non-linearities and holes that occur in latent spaces, whilst minimising unwanted changes to other attributes. This paper introduces SeNT-Gen, a neural traversal algorithm that uses a secondary neural network to model the complex relationships between latent codes and musical attributes. This enables precise editing of semantic attributes that adapts to context. We demonstrate the method using the dMelodies dataset, and show strong performance for several VAE models.''', 
    tags = [ismir2022, control], 
    my_notes = r'''
if irrelevant dims should stay constant, why not prescribe?
limitations: all factors in the data are known, i.e., $c$ fully characterizes data.  
    when you require "change this and leave the rest unchanged", you have full knowledge of what "the rest" are. 
    rho: is it even right?
        if two factors are correlated, you can still disentangle. rho allows correlated dimensions to change. 
        the baseline would be `rho=1` always. Consider dimensions where z** != z*. z** is the "actually correct" z*. 
        given such a toy dataset, the only role of rho is to "clip" dimensions that are off because of data availablity. 
''', 
)

haptic_guidance_benefits_musical_motor_learning = Paper(
    apa = r'''Grindlay, G. (2008, March). Haptic guidance benefits musical motor learning. In 2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems (pp. 397-404). IEEE.''', 
    bib = None, 
    abstract = r'''This paper presents the results of a pilot experiment looking at the effect of haptic guidance on musical training. A percussion performance task was used where subjects learned to play short rhythmic sequences on a device capable of recording drumstick movements with a high degree of spatiotemporal accuracy. Subjects learned to perform the sequences under three primary training paradigms: listening to the rhythm (audio), being guided through the motions involved in the rhythm's performance (haptic), and being guided through the required motions while listening to the resulting sound (audio+haptic). Performance was assessed in terms of both timing and loudness (velocity) accuracy using several different metrics. Results indicate that haptic guidance can significantly benefit recall of both note timing and velocity. When subject performance was compared in terms of note velocity recall, the addition of haptic guidance to audio-based training produced a 17% reduction in final error when compared to audio training alone. When performance was evaluated in terms of liming recall, the combination of audio and haptic guidance led to an 18% reduction in early-stage error.''', 
    tags = [haptic], 
    my_notes = r'''
cited in nime22 "A Computer-aided Multimodal Music Learning System with Curriculum: A Pilot Study"
Check "related works" section for a summary. 
''', 
)

haptic_technology_in_digital_music_learning_context_a_state_of_the_art_analysis = Paper(
    apa = r'''Dörr, B., Norouzinia, F., Altmeyer, K., & Werth, D. (2022, October). Haptic Technology in Digital Music Learning Context: A State-of-the-Art Analysis. In European Conference on e-Learning (Vol. 21, No. 1, pp. 87-94). Academic Conferences International Limited.''', 
    bib = r'''@inproceedings{dorr2022haptic,
  title={Haptic Technology in Digital Music Learning Context: A State-of-the-Art Analysis},
  author={D{\"o}rr, Bianka and Norouzinia, Farzaneh and Altmeyer, Kristin and Werth, Dirk},
  booktitle={European Conference on e-Learning},
  volume={21},
  number={1},
  pages={87--94},
  year={2022},
  organization={Academic Conferences International Limited}
}''', 
    abstract = r'''Digital media have become increasingly established in learning contexts in recent decades, and it seems impossibleto imagine education without them, especially in recent years. Various technological advances can be observed, such asdevelopments in virtual reality and augmented reality. To give learners a realistic impression of the virtual world, as manysensory impressions as possible should be addressed. However, current developments have mainly addressed the visual andauditory modalities, which make up two of the five human senses. Research and developments for the use of the othersenses are being made but at this stage they are not yet ready for mass use. Especially the sense of touch based on skin asthe largest human sensory organ or tactile and haptic perception seem to be of interest. Particularly in manual or medicalareas where motor skills are required, haptic technologies are declared to be supportive and beneficial. One area that hashardly focused on digital learning so far is the music sector. Learning a musical instrument in this context seems to be aninteresting field of research, as it not only promotes motor skills, but also cognitive development in both children and adults.To give an update on the technical developments in the field of digital teaching and learning in music, and especially tohighlight the use of haptic technologies, we will briefly review the state of the art in this paper. It begins with a brief overviewof the basics of digital learning and haptics, as well as previous work in this field. Using the method of a scoping review, thetopic of haptic technologies in the field of music education will be researched, analysed, and summarised according todefined criteria to give a condensed overview of it. The selected database and appropriate search strings will be used toachieve the aim of the paper. The results help to shed light on current research gaps and give indications for futuredevelopments of haptic technology in the music learning context.''', 
    tags = [], 
)

unsupervised_latent_tree_induction_with_deep_inside_outside_recursive_autoencoders = Paper(
    apa = r'''Drozdov, A., Verga, P., Yadav, M., Iyyer, M., & McCallum, A. (2019). Unsupervised latent tree induction with deep inside-outside recursive autoencoders. arXiv preprint arXiv:1904.02142.''', 
    bib = r'''@article{drozdov2019unsupervised,
  title={Unsupervised latent tree induction with deep inside-outside recursive autoencoders},
  author={Drozdov, Andrew and Verga, Pat and Yadav, Mohit and Iyyer, Mohit and McCallum, Andrew},
  journal={arXiv preprint arXiv:1904.02142},
  year={2019}
}''', 
    abstract = r'''We introduce deep inside-outside recursive autoencoders (DIORA), a fully-unsupervised method for discovering syntax that simultaneously learns representations for constituents within the induced tree. Our approach predicts each word in an input sentence conditioned on the rest of the sentence and uses inside-outside dynamic programming to consider all possible binary trees over the sentence. At test time the CKY algorithm extracts the highest scoring parse. DIORA achieves a new state-of-the-art F1 in unsupervised binary constituency parsing (unlabeled) in two benchmark datasets, WSJ and MultiNLI.''', 
    tags = [self_supervise, repr_learning], 
)

vicreg_variance_invariance_covariance_regularization_for_self_supervised_learning = Paper(
    apa = r'''Bardes, A., Ponce, J., & LeCun, Y. (2021). Vicreg: Variance-invariance-covariance regularization for self-supervised learning. arXiv preprint arXiv:2105.04906.''', 
    bib = r'''@article{bardes2021vicreg,
  title={Vicreg: Variance-invariance-covariance regularization for self-supervised learning},
  author={Bardes, Adrien and Ponce, Jean and LeCun, Yann},
  journal={arXiv preprint arXiv:2105.04906},
  year={2021}
}''', 
    abstract = r'''Recent self-supervised methods for image representation learning are based on maximizing the agreement between embedding vectors from different views of the same image. A trivial solution is obtained when the encoder outputs constant vectors. This collapse problem is often avoided through implicit biases in the learning architecture, that often lack a clear justification or interpretation. In this paper, we introduce VICReg (Variance-Invariance-Covariance Regularization), a method that explicitly avoids the collapse problem with a simple regularization term on the variance of the embeddings along each dimension individually. VICReg combines the variance term with a decorrelation mechanism based on redundancy reduction and covariance regularization, and achieves results on par with the state of the art on several downstream tasks. In addition, we show that incorporating our new variance term into other methods helps stabilize the training and leads to performance improvements.''', 
    tags = [self_supervise, jepa_or_jem], 
    my_notes = r'''
why need expander? what's the diff between repr and emb? 
"expander ... eliminate the information by which the two representations differ"
    strange. 
    - you are trying to train the repr, not the emb, to be good. 
    - invariance ("s" in fig 1) makes sense, and should apply to repr. 
    - you are allowing repr to be sensitive to e.g. data aug, but emb should not? 
"expander ... expand the dimension in a non-linear
fashion so that decorrelating the embedding variables will reduce the dependencies (not just the
correlations) between the variables of the representation vector. "
    what? sounds like you need adverserial training. 
    optim the expander to maximize covariance. 
    optim the encoder to minimize covariance. 
    (ensemble of expanders?)
    if there is no adversetial training, wouldn't covariance just encourage the expander to scramble the repr into non-linear emb? 
''', 
)

barlow_twins_self_supervised_learning_via_redundancy_reduction = Paper(
    apa = r'''Zbontar, J., Jing, L., Misra, I., LeCun, Y., & Deny, S. (2021, July). Barlow twins: Self-supervised learning via redundancy reduction. In International Conference on Machine Learning (pp. 12310-12320). PMLR.''', 
    bib = r'''@inproceedings{zbontar2021barlow,
  title={Barlow twins: Self-supervised learning via redundancy reduction},
  author={Zbontar, Jure and Jing, Li and Misra, Ishan and LeCun, Yann and Deny, St{\'e}phane},
  booktitle={International Conference on Machine Learning},
  pages={12310--12320},
  year={2021},
  organization={PMLR}
}''', 
    abstract = r'''Self-supervised learning (SSL) is rapidly closing the gap with supervised methods on large computer vision benchmarks. A successful approach to SSL is to learn embeddings which are invariant to distortions of the input sample. However, a recurring issue with this approach is the existence of trivial constant solutions. Most current methods avoid such solutions by careful implementation details. We propose an objective function that naturally avoids collapse by measuring the cross-correlation matrix between the outputs of two identical networks fed with distorted versions of a sample, and making it as close to the identity matrix as possible. This causes the embedding vectors of distorted versions of a sample to be similar, while minimizing the redundancy between the components of these vectors. The method is called Barlow Twins, owing to neuroscientist H. Barlow’s redundancy-reduction principle applied to a pair of identical networks. Barlow Twins does not require large batches nor asymmetry between the network twins such as a predictor network, gradient stopping, or a moving average on the weight updates. Intriguingly it benefits from very high-dimensional output vectors. Barlow Twins outperforms previous methods on ImageNet for semi-supervised classification in the low-data regime, and is on par with current state of the art for ImageNet classification with a linear classifier head, and for transfer tasks of classification and object detection.''', 
    tags = [self_supervise, jepa_or_jem], 
    my_notes = r'''
Diff w/ VICReg: *Cross*-correlation between Z_A and Z_B.  
''', 
)

a_simple_framework_for_contrastive_learning_of_visual_representations = Paper(
    shorts = ['SimCLR'], 
    apa = r'''Chen, T., Kornblith, S., Norouzi, M., & Hinton, G. (2020, November). A simple framework for contrastive learning of visual representations. In International conference on machine learning (pp. 1597-1607). PMLR.''', 
    bib = r'''@inproceedings{chen2020simple,
  title={A simple framework for contrastive learning of visual representations},
  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
  booktitle={International conference on machine learning},
  pages={1597--1607},
  year={2020},
  organization={PMLR}
}''', 
    abstract = r'''This paper presents SimCLR: a simple framework for contrastive learning of visual representations. We simplify recently proposed contrastive self-supervised learning algorithms without requiring specialized architectures or a memory bank. In order to understand what enables the contrastive prediction tasks to learn useful representations, we systematically study the major components of our framework. We show that (1) composition of data augmentations plays a critical role in defining effective predictive tasks, (2) introducing a learnable nonlinear transformation between the representation and the contrastive loss substantially improves the quality of the learned representations, and (3) contrastive learning benefits from larger batch sizes and more training steps compared to supervised learning. By combining these findings, we are able to considerably outperform previous methods for self-supervised and semi-supervised learning on ImageNet. A linear classifier trained on self-supervised representations learned by SimCLR achieves 76.5% top-1 accuracy, which is a 7% relative improvement over previous state-of-the-art, matching the performance of a supervised ResNet-50. When fine-tuned on only 1% of the labels, we achieve 85.8% top-5 accuracy, outperforming AlexNet with 100X fewer labels.''', 
    tags = [self_supervise, jepa_or_jem, contrastive], 
    my_notes = r'''
Diff w/ VICReg: 
    need to compute the denominator (negative pairs) for every datapoint within a batch. 
    VICReg only compute VIC once per batch. 
''', 
)

momentum_contrast_for_unsupervised_visual_representation_learning = Paper(
    shorts = ['MoCo'], 
    apa = r'''He, K., Fan, H., Wu, Y., Xie, S., & Girshick, R. (2020). Momentum contrast for unsupervised visual representation learning. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (pp. 9729-9738).''', 
    bib = r'''@inproceedings{he2020momentum,
  title={Momentum contrast for unsupervised visual representation learning},
  author={He, Kaiming and Fan, Haoqi and Wu, Yuxin and Xie, Saining and Girshick, Ross},
  booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
  pages={9729--9738},
  year={2020}
}''', 
    abstract = r'''We present Momentum Contrast (MoCo) for unsupervised visual representation learning. From a perspective on contrastive learning as dictionary look-up, we build a dynamic dictionary with a queue and a moving-averaged encoder. This enables building a large and consistent dictionary on-the-fly that facilitates contrastive unsupervised learning. MoCo provides competitive results under the common linear protocol on ImageNet classification. More importantly, the representations learned by MoCo transfer well to downstream tasks. MoCo can outperform its supervised pre-training counterpart in 7 detection/segmentation tasks on PASCAL VOC, COCO, and other datasets, sometimes surpassing it by large margins. This suggests that the gap between unsupervised and supervised representation learning has been largely closed in many vision tasks.''', 
    tags = [self_supervise, jepa_or_jem, contrastive], 
)

representation_learning_with_contrastive_predictive_coding = Paper(
    shorts = ['infoNCE', 'CPC'], 
    apa = r'''Oord, A. V. D., Li, Y., & Vinyals, O. (2018). Representation learning with contrastive predictive coding. arXiv preprint arXiv:1807.03748.''', 
    bib = r'''@article{oord2018representation,
  title={Representation learning with contrastive predictive coding},
  author={Oord, Aaron van den and Li, Yazhe and Vinyals, Oriol},
  journal={arXiv preprint arXiv:1807.03748},
  year={2018}
}''', 
    abstract = r'''While supervised learning has enabled great progress in many applications, unsupervised learning has not seen such widespread adoption, and remains an important and challenging endeavor for artificial intelligence. In this work, we propose a universal unsupervised learning approach to extract useful representations from high-dimensional data, which we call Contrastive Predictive Coding. The key insight of our model is to learn such representations by predicting the future in latent space by using powerful autoregressive models. We use a probabilistic contrastive loss which induces the latent space to capture information that is maximally useful to predict future samples. It also makes the model tractable by using negative sampling. While most prior work has focused on evaluating representations for a particular modality, we demonstrate that our approach is able to learn useful representations achieving strong performance on four distinct domains: speech, images, text and reinforcement learning in 3D environments.''', 
    tags = [self_supervise, jepa_or_jem, contrastive], 
)

whitening_for_self_supervised_representation_learning = Paper(
    apa = r'''Ermolov, A., Siarohin, A., Sangineto, E., & Sebe, N. (2021, July). Whitening for self-supervised representation learning. In International Conference on Machine Learning (pp. 3015-3024). PMLR.''', 
    bib = r'''@inproceedings{ermolov2021whitening,
  title={Whitening for self-supervised representation learning},
  author={Ermolov, Aleksandr and Siarohin, Aliaksandr and Sangineto, Enver and Sebe, Nicu},
  booktitle={International Conference on Machine Learning},
  pages={3015--3024},
  year={2021},
  organization={PMLR}
}''', 
    abstract = r'''Most of the current self-supervised representation learning (SSL) methods are based on the contrastive loss and the instance-discrimination task, where augmented versions of the same image instance ("positives") are contrasted with instances extracted from other images ("negatives"). For the learning to be effective, many negatives should be compared with a positive pair, which is computationally demanding. In this paper, we propose a different direction and a new loss function for SSL, which is based on the whitening of the latent-space features. The whitening operation has a "scattering" effect on the batch samples, avoiding degenerate solutions where all the sample representations collapse to a single point. Our solution does not require asymmetric networks and it is conceptually simple. Moreover, since negatives are not needed, we can extract multiple positive pairs from the same image instance. The source code of the method and of all the experiments is available at: https://github.com/htdt/self-supervised.''', 
    tags = [self_supervise, jepa_or_jem], 
)

bootstrap_your_own_latent_a_new_approach_to_self_supervised_learning = Paper(
    apa = r'''Grill, J. B., Strub, F., Altché, F., Tallec, C., Richemond, P., Buchatskaya, E., ... & Valko, M. (2020). Bootstrap your own latent-a new approach to self-supervised learning. Advances in neural information processing systems, 33, 21271-21284.''', 
    bib = r'''@article{grill2020bootstrap,
  title={Bootstrap your own latent-a new approach to self-supervised learning},
  author={Grill, Jean-Bastien and Strub, Florian and Altch{\'e}, Florent and Tallec, Corentin and Richemond, Pierre and Buchatskaya, Elena and Doersch, Carl and Avila Pires, Bernardo and Guo, Zhaohan and Gheshlaghi Azar, Mohammad and others},
  journal={Advances in neural information processing systems},
  volume={33},
  pages={21271--21284},
  year={2020}
}''', 
    abstract = r'''We introduce Bootstrap Your Own Latent (BYOL), a new approach to self-supervised image representation learning. BYOL relies on two neural networks, referred to as online and target networks, that interact and learn from each other. From an augmented view of an image, we train the online network to predict the target network representation of the same image under a different augmented view. At the same time, we update the target network with a slow-moving average of the online network. While state-of-the art methods intrinsically rely on negative pairs, BYOL achieves a new state of the art without them. BYOL reaches 74.3% top-1 classification accuracy on ImageNet using the standard linear evaluation protocol with a standard ResNet-50 architecture and 79.6% with a larger ResNet. We also show that BYOL performs on par or better than the current state of the art on both transfer and semi-supervised benchmarks.''', 
    tags = [self_supervise, jepa_or_jem], 
)

exploring_simple_siamese_representation_learning = Paper(
    shorts = ['SimSiam'], 
    apa = r'''Chen, X., & He, K. (2021). Exploring simple siamese representation learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 15750-15758).''', 
    bib = r'''@inproceedings{chen2021exploring,
  title={Exploring simple siamese representation learning},
  author={Chen, Xinlei and He, Kaiming},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={15750--15758},
  year={2021}
}''', 
    abstract = r'''Siamese networks have become a common structure in various recent models for unsupervised visual representation learning. These models maximize the similarity between two augmentations of one image, subject to certain conditions for avoiding collapsing solutions. In this paper, we report surprising empirical results that simple Siamese networks can learn meaningful representations even using none of the following: (i) negative sample pairs, (ii) large batches, (iii) momentum encoders. Our experiments show that collapsing solutions do exist for the loss and structure, but a stop-gradient operation plays an essential role in preventing collapsing. We provide a hypothesis on the implication of stop-gradient, and further show proof-of-concept experiments verifying it. Our "SimSiam" method achieves competitive results on ImageNet and downstream tasks. We hope this simple baseline will motivate people to rethink the roles of Siamese architectures for unsupervised representation learning. Code is made available. (https://github.com/facebookresearch/simsiam)''', 
    tags = [self_supervise, jepa_or_jem], 
)

unsupervised_learning_of_visual_features_by_contrasting_cluster_assignments = Paper(
    shorts = ['SwAV'], 
    apa = r'''Caron, M., Misra, I., Mairal, J., Goyal, P., Bojanowski, P., & Joulin, A. (2020). Unsupervised learning of visual features by contrasting cluster assignments. Advances in Neural Information Processing Systems, 33, 9912-9924.''', 
    bib = r'''@article{caron2020unsupervised,
  title={Unsupervised learning of visual features by contrasting cluster assignments},
  author={Caron, Mathilde and Misra, Ishan and Mairal, Julien and Goyal, Priya and Bojanowski, Piotr and Joulin, Armand},
  journal={Advances in Neural Information Processing Systems},
  volume={33},
  pages={9912--9924},
  year={2020}
}''', 
    abstract = r'''Unsupervised image representations have significantly reduced the gap with supervised pretraining, notably with the recent achievements of contrastive learning methods. These contrastive methods typically work online and rely on a large number of explicit pairwise feature comparisons, which is computationally challenging. In this paper, we propose an online algorithm, SwAV, that takes advantage of contrastive methods without requiring to compute pairwise comparisons. Specifically, our method simultaneously clusters the data while enforcing consistency between cluster assignments produced for different augmentations (or views) of the same image, instead of comparing features directly as in contrastive learning. Simply put, we use a swapped prediction mechanism where we predict the code of a view from the representation of another view. Our method can be trained with large and small batches and can scale to unlimited amounts of data. Compared to previous contrastive methods, our method is more memory efficient since it does not require a large memory bank or a special momentum network. In addition, we also propose a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. We validate our findings by achieving 75.3% top-1 accuracy on ImageNet with ResNet-50, as well as surpassing supervised pretraining on all the considered transfer tasks.''', 
    tags = [self_supervise, jepa_or_jem], 
)

a_unified_model_for_zero_shot_music_source_separation_transcription_and_synthesis = Paper(
    apa = r'''Lin, L., Kong, Q., Jiang, J., & Xia, G. (2021). A unified model for zero-shot music source separation, transcription and synthesis. arXiv preprint arXiv:2108.03456.''', 
    bib = r'''@article{lin2021unified,
  title={A unified model for zero-shot music source separation, transcription and synthesis},
  author={Lin, Liwei and Kong, Qiuqiang and Jiang, Junyan and Xia, Gus},
  journal={arXiv preprint arXiv:2108.03456},
  year={2021}
}''', 
    abstract = r'''We propose a unified model for three inter-related tasks: 1) to 	extit{separate} individual sound sources from a mixed music audio, 2) to 	extit{transcribe} each sound source to MIDI notes, and 3) to	extit{ synthesize} new pieces based on the timbre of separated sources. The model is inspired by the fact that when humans listen to music, our minds can not only separate the sounds of different instruments, but also at the same time perceive high-level representations such as score and timbre. To mirror such capability computationally, we designed a pitch-timbre disentanglement module based on a popular encoder-decoder neural architecture for source separation. The key inductive biases are vector-quantization for pitch representation and pitch-transformation invariant for timbre representation. In addition, we adopted a query-by-example method to achieve 	extit{zero-shot} learning, i.e., the model is capable of doing source separation, transcription, and synthesis for 	extit{unseen} instruments. The current design focuses on audio mixtures of two monophonic instruments. Experimental results show that our model outperforms existing multi-task baselines, and the transcribed score serves as a powerful auxiliary for separation tasks.''', 
    tags = [self_supervise, music_knowledge, f0, multi_source_seperation, zero_shot, pitch_shift_invariance], 
)

blip_2_bootstrapping_language_image_pre_training_with_frozen_image_encoders_and_large_language_models = Paper(
    apa = r'''Li, J., Li, D., Savarese, S., & Hoi, S. (2023). Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. arXiv preprint arXiv:2301.12597.''', 
    bib = r'''@article{li2023blip,
  title={Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models},
  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},
  journal={arXiv preprint arXiv:2301.12597},
  year={2023}
}''', 
    abstract = r'''The cost of vision-and-language pre-training has become increasingly prohibitive due to end-to-end training of large-scale models. This paper proposes BLIP-2, a generic and efficient pre-training strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models. BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pre-trained in two stages. The first stage bootstraps vision-language representation learning from a frozen image encoder. The second stage bootstraps vision-to-language generative learning from a frozen language model. BLIP-2 achieves state-of-the-art performance on various vision-language tasks, despite having significantly fewer trainable parameters than existing methods. For example, our model outperforms Flamingo80B by 8.7% on zero-shot VQAv2 with 54x fewer trainable parameters. We also demonstrate the model's emerging capabilities of zero-shot image-to-text generation that can follow natural language instructions.''', 
    tags = [llm, hyper_network, contrastive], 
    my_notes = r'''
Nearest neighbor (English words) of the image feature seq.  
Ablate: use text instead of image features to prompt LLM.  
''', 
)

generative_agents_interactive_simulacra_of_human_behavior = Paper(
    apa = r'''Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. arXiv preprint arXiv:2304.03442.''', 
    bib = r'''@article{park2023generative,
  title={Generative agents: Interactive simulacra of human behavior},
  author={Park, Joon Sung and O'Brien, Joseph C and Cai, Carrie J and Morris, Meredith Ringel and Liang, Percy and Bernstein, Michael S},
  journal={arXiv preprint arXiv:2304.03442},
  year={2023}
}''', 
    abstract = r'''Believable proxies of human behavior can empower interactive applications ranging from immersive environments to rehearsal spaces for interpersonal communication to prototyping tools. In this paper, we introduce generative agents--computational software agents that simulate believable human behavior. Generative agents wake up, cook breakfast, and head to work; artists paint, while authors write; they form opinions, notice each other, and initiate conversations; they remember and reflect on days past as they plan the next day. To enable generative agents, we describe an architecture that extends a large language model to store a complete record of the agent's experiences using natural language, synthesize those memories over time into higher-level reflections, and retrieve them dynamically to plan behavior. We instantiate generative agents to populate an interactive sandbox environment inspired by The Sims, where end users can interact with a small town of twenty five agents using natural language. In an evaluation, these generative agents produce believable individual and emergent social behaviors: for example, starting with only a single user-specified notion that one agent wants to throw a Valentine's Day party, the agents autonomously spread invitations to the party over the next two days, make new acquaintances, ask each other out on dates to the party, and coordinate to show up for the party together at the right time. We demonstrate through ablation that the components of our agent architecture--observation, planning, and reflection--each contribute critically to the believability of agent behavior. By fusing large language models with computational, interactive agents, this work introduces architectural and interaction patterns for enabling believable simulations of human behavior.''', 
    tags = [llm, llm_add_system_2, llm_in_the_loop], 
)

haptic_training_which_types_facilitate_re_learning_of_which_motor_task_and_for_whom_answers_by_a_review = Paper(
    apa = r'''Basalp, E., Wolf, P., & Marchal-Crespo, L. (2021). Haptic training: which types facilitate (re) learning of which motor task and for whom? answers by a review. IEEE transactions on haptics, 14(4), 722-739.''', 
    bib = r'''@article{basalp2021haptic,
  title={Haptic training: which types facilitate (re) learning of which motor task and for whom? answers by a review},
  author={Basalp, Ekin and Wolf, Peter and Marchal-Crespo, Laura},
  journal={IEEE transactions on haptics},
  volume={14},
  number={4},
  pages={722--739},
  year={2021},
  publisher={IEEE}
}''', 
    abstract = r'''The use of robots has attracted researchers to design numerous haptic training methods to support motor learning. However, investigations of new methods yielded inconclusive results regarding their effectiveness to enhance learning due to the diversity of tasks, haptic designs, participants’ skill level, and study protocols. In this review, we developed a taxonomy to identify generalizable findings out of publications on haptic training. In the taxonomy, we grouped the results of studies on healthy learners based on participants’ skill level and tasks’ characteristics. Our inspection of included studies revealed that: i) Performance-enhancing haptic methods were beneficial for novices, ii) Training with haptics was as effective as training with other feedback modalities, and iii) Performance-enhancing and performance-degrading haptic methods were useful for the learning of temporal and spatial aspects, respectively. We also observed that these findings are in line with results from robot-aided neurorehabilitation studies on patients. Our review suggests that haptic training can be effective to foster learning, especially when the information cannot be provided with other feedback modalities. We believe the findings from the taxonomy constitute a general guide, which can assist researchers when designing studies to investigate the effectiveness of haptics on learning different tasks.''', 
    tags = [haptic, education, psychology], 
)

musicjacket_combining_motion_capture_and_vibrotactile_feedback_to_teach_violin_bowing = Paper(
    apa = r'''Van Der Linden, J., Schoonderwaldt, E., Bird, J., & Johnson, R. (2010). Musicjacket—combining motion capture and vibrotactile feedback to teach violin bowing. IEEE Transactions on Instrumentation and Measurement, 60(1), 104-113.''', 
    bib = r'''@article{van2010musicjacket,
  title={Musicjacket—combining motion capture and vibrotactile feedback to teach violin bowing},
  author={Van Der Linden, Janet and Schoonderwaldt, Erwin and Bird, Jon and Johnson, Rose},
  journal={IEEE Transactions on Instrumentation and Measurement},
  volume={60},
  number={1},
  pages={104--113},
  year={2010},
  publisher={IEEE}
}''', 
    abstract = r'''We describe MusicJacket, which is a wearable system to support the teaching of good posture and bowing technique to novice violin players. The system uses an inertial motion capture system to track the following in real time: 1) whether the player is holding the violin correctly and 2) the player's bowing action and whether it deviates from a target trajectory. We provide the musicians with vibrotactile feedback about their bowing and posture using vibration motors that are positioned on their arms and torso. We describe a user study with novice violin players that compared a group who was trained using vibrotactile feedback with a control group who only received conventional teaching. We found that vibrotactile feedback is effective at improving novices' straight bowing technique and that half of these subjects continued to show improved bowing technique even when they no longer received vibrotactile feedback. None of the control subjects who received the same number of training sessions using conventional teaching techniques showed a comparable improvement.''', 
    tags = [haptic, education, vibration], 
)

towards_passive_haptic_learning_of_piano_songs = Paper(
    apa = r'''Seim, C., Estes, T., & Starner, T. (2015, June). Towards passive haptic learning of piano songs. In 2015 IEEE World Haptics Conference (WHC) (pp. 445-450). IEEE.''', 
    bib = r'''@inproceedings{seim2015towards,
  title={Towards passive haptic learning of piano songs},
  author={Seim, Caitlyn and Estes, Tanya and Starner, Thad},
  booktitle={2015 IEEE World Haptics Conference (WHC)},
  pages={445--450},
  year={2015},
  organization={IEEE}
}''', 
    abstract = r'''Passive Haptic Learning (PHL) enables users to acquire motor skills by receiving tactile stimulation while no perceived attention is given to learning. Initial work used gloves with embedded vibration motors to passively teach users how to play simple, one-handed, one-note-at-a-time piano melodies. In an effort to create a practical system for learning full piano pieces, we have developed a method of passively teaching two-handed chorded skills, initially focusing on Braille typing. Here, we extend this effort to piano and show that passive stimulation is more effective at teaching piano pieces when presented on both hands simultaneously as opposed to training the left hand and then the right, as is common in many active teaching methods. We also demonstrate that accompanying audio is not needed for passive learning of piano melodies, which allows mobile PHL gloves to be used in more everyday situations.''', 
    tags = [haptic, education, passive_learning, vibration], 
    my_notes = r'''
In addition to its abstract:  
2x2 (A, H) piano passive reviewing  
''', 
)

passive_haptic_learning_of_braille_typing = Paper(
    apa = r'''Seim, C., Chandler, J., DesPortes, K., Dhingra, S., Park, M., & Starner, T. (2014, September). Passive haptic learning of Braille typing. In Proceedings of the 2014 ACM International Symposium on Wearable Computers (pp. 111-118).''', 
    bib = r'''@inproceedings{seim2014passive,
  title={Passive haptic learning of Braille typing},
  author={Seim, Caitlyn and Chandler, John and DesPortes, Kayla and Dhingra, Siddharth and Park, Miru and Starner, Thad},
  booktitle={Proceedings of the 2014 ACM International Symposium on Wearable Computers},
  pages={111--118},
  year={2014}
}''', 
    abstract = r'''Passive Haptic Learning (PHL) is the acquisition of sensorimotor skills without active attention to learning. One method is to "teach" motor skills using vibration cues delivered by a wearable, tactile interface while the user is focusing on another, primary task. We have created a system for Passive Haptic Learning of typing skills. In a study containing 16 participants, users demonstrated significantly reduced error typing a phrase in Braille after receiving passive instruction versus control (32.85% average decline in error vs. 2.73% increase in error). PHL users were also able to recognize and read more Braille letters from the phrase (72.5% vs. 22.4%). In a second study, containing 8 participants thus far, we passively teach the full Braille alphabet over four sessions. Typing error reductions in participants receiving PHL were more rapid and consistent, with 75% of PHL vs. 0% of control users reaching zero typing error. By the end of the study, PHL participants were also able to recognize and read 93.3% of all Braille alphabet letters. These results suggest that Passive Haptic instruction facilitated by wearable computers may be a feasible method of teaching Braille typing and reading.''', 
    tags = [haptic, education, passive_learning, vibration], 
    my_notes = r'''
Passive haptic learning successfully teaching novel mappings?  
Stimuli: coordinated H and A (spoken letter).  
Is contrary to our results.  
Also, staggering simultaneous haptic stimuli may help, (consistent w/ our haptic hat findings).  
''', 
)

computer_assisted_music_instructment_tutoring_applied_to_violin_practice = Paper(
    apa = r'''Huanhuan, L. (2009). Computer assisted music instructment tutoring applied to violin practice.''', 
    bib = r'''@article{huanhuan2009computer,
  title={Computer assisted music instructment tutoring applied to violin practice},
  author={Huanhuan, Lu},
  year={2009}
}''', 
    abstract = None, 
    tags = [], 
    my_notes = r'''
A thesis. No haptic feedback.  
''', 
)

haptic_learning_and_how_it_can_enhance_digital_learning_experiences_an_innovative_approach = Paper(
    apa = r'''Dörr, B., Funk, M., Norouzinia, F., & Werth, D. (2022). Haptic learning and how it can enhance digital learning experiences: an innovative approach. In INTED2022 Proceedings (pp. 3909-3917). IATED.''', 
    bib = r'''@inproceedings{dorr2022haptic,
  title={Haptic learning and how it can enhance digital learning experiences: an innovative approach},
  author={D{\"o}rr, B and Funk, M and Norouzinia, F and Werth, D},
  booktitle={INTED2022 Proceedings},
  pages={3909--3917},
  year={2022},
  organization={IATED}
}''', 
    abstract = r'''Digital learning has increased rapidly in the recent years but has primarily focused on teaching knowledge, using auditory and visual modalities. However, the use of haptic modalities has been hardly considered so far, even though it would be particularly interesting for the learning of skills and processes. Especially in the medical field, it is shown e.g., that the addition of haptic feedback in a virtual learning environment can have a positive influence on the learning of skills.
In order to take a further step towards the inclusion of haptics in teaching and learning processes, we want to give an overview of our understanding of haptic learning in this paper. We will do this by presenting our definition of haptic learning with corresponding delimitations and by introducing our model of haptic learning. The model will be explained by describing its structure with its three core areas and justifying why each of these areas is meaningful for haptic learning or why we have chosen them accordingly. This model is an attempt to relate different concepts of haptics to each other, especially the understanding of haptic learning, and to look at it from a broader holistic perspective. The aim is to make use cases in practice more describable and analyzable and to show the range of possible applications for haptic learning. Furthermore, in addition to the evaluation of use cases, it should be possible to optimize them with regard to learning effectiveness and efficiency. Also, we will have a closer look at the models’ features by which use cases can be analyzed and characterized to make haptic learning systematically describable. Based on these features some use cases will be analyzed as a next step to demonstrate their application. Finally, a summary of the paper and an outlook will be given to demonstrate the potential of our model for digital use cases of haptic learning.
''', 
    tags = [haptic, education], 
    my_notes = r'''
I see limited usability of their model.  
''', 
)

haptic_learning_and_technology_analyses_of_digital_use_cases_of_haptics_using_the_haptic_learning_model = Paper(
    apa = r'''Norouzinia, F., Dörr, B., Funk, M., & Werth, D. (2022, June). Haptic learning and technology: Analyses of digital use cases of haptics using the haptic learning model. In HCI International 2022 Posters: 24th International Conference on Human-Computer Interaction, HCII 2022, Virtual Event, June 26–July 1, 2022, Proceedings, Part III (pp. 72-79). Cham: Springer International Publishing.''', 
    bib = r'''@inproceedings{norouzinia2022haptic,
  title={Haptic learning and technology: Analyses of digital use cases of haptics using the haptic learning model},
  author={Norouzinia, Farzaneh and D{\"o}rr, Bianka and Funk, Mareike and Werth, Dirk},
  booktitle={HCI International 2022 Posters: 24th International Conference on Human-Computer Interaction, HCII 2022, Virtual Event, June 26--July 1, 2022, Proceedings, Part III},
  pages={72--79},
  year={2022},
  organization={Springer}
}''', 
    abstract = r'''Learning with involvement of haptic technologies can provide advanced opportunities in digital learning. Especially over the course of the pandemic the value of digital learning solutions became more obvious. There are attempts with various technologies, which can enhance the quality of learning processes and refine the learning results. However, it should be remembered that the sense of touch is not contained in all of them, even though it might be helpful, e.g., in the medical field. To show how haptic technology may improve the digital learning solutions, this paper will briefly define haptic learning and analyze some haptic learning use cases using the Haptic Learning Model of Dörr et al. [2].
We describe haptic learning as the sum of all learning processes which use haptic interactions to enhance the effectiveness and/or efficiency of learning process. In this paper, haptic technology use cases which are not directly related to learning or do not give any haptic feedback to the learners are excluded.
''', 
    tags = [haptic, education], 
    my_notes = r'''
Using the model proposed by computer_assisted_music_instructment_tutoring_applied_to_violin_practice.  
''', 
)

passive_somatosensory_training_enhances_piano_skill_in_adolescent_and_adult_pianists_a_preliminary_study = Paper(
    apa = r'''Furuya, S., Tanibuchi, R., Nishioka, H., Kimoto, Y., Hirano, M., & Oku, T. (2023). Passive somatosensory training enhances piano skill in adolescent and adult pianists: A preliminary study. Annals of the New York Academy of Sciences, 1519(1), 167-172.''', 
    bib = r'''@article{furuya2023passive,
  title={Passive somatosensory training enhances piano skill in adolescent and adult pianists: A preliminary study},
  author={Furuya, Shinichi and Tanibuchi, Ryuya and Nishioka, Hayato and Kimoto, Yudai and Hirano, Masato and Oku, Takanori},
  journal={Annals of the New York Academy of Sciences},
  volume={1519},
  number={1},
  pages={167--172},
  year={2023},
  publisher={Wiley Online Library}
}''', 
    abstract = r'''Sensory afferent information, such as auditory and somatosensory feedback while moving, plays a crucial role in both control and learning of motor performance across the lifespan. Music performance requires skillful integration of multimodal sensory information for the production of dexterous movements. However, it has not been understood what roles somatosensory afferent information plays in the acquisition and sophistication of specialized motor skills of musicians across different stages of development. In the present preliminary study, we addressed this issue by using a novel technique with a hand exoskeleton robot that can externally move the fingers of pianists. Short-term exposure to fast and complex finger movements generated by the exoskeleton (i.e., passive movements) increased the maximum rate of repetitive piano keystrokes by the pianists. This indicates that somatosensory inputs derived from the externally generated motions enhanced the quickness of the sequential finger movements in piano performance, even though the pianists did not voluntarily move the fingers. The enhancement of motor skill through passive somatosensory training using the exoskeleton was more pronounced in adolescent pianists than adult pianists. These preliminary results implicate a sensitive period of neuroplasticity of the somatosensory-motor system of trained pianists, which emphasizes the importance of somatosensory-motor training in professional music education during adolescence.''', 
    tags = [haptic, education], 
    my_notes = r'''Piano skill: press a key really fast''', 
)

augmented_visual_auditory_haptic_and_multimodal_feedback_in_motor_learning_a_review = Paper(
    apa = r'''Sigrist, R., Rauter, G., Riener, R., & Wolf, P. (2013). Augmented visual, auditory, haptic, and multimodal feedback in motor learning: a review. Psychonomic bulletin & review, 20, 21-53.''', 
    bib = r'''@article{sigrist2013augmented,
  title={Augmented visual, auditory, haptic, and multimodal feedback in motor learning: a review},
  author={Sigrist, Roland and Rauter, Georg and Riener, Robert and Wolf, Peter},
  journal={Psychonomic bulletin \& review},
  volume={20},
  pages={21--53},
  year={2013},
  publisher={Springer}
}''', 
    abstract = r'''It is generally accepted that augmented feedback, provided by a human expert or a technical display, effectively enhances motor learning. However, discussion of the way to most effectively provide augmented feedback has been controversial. Related studies have focused primarily on simple or artificial tasks enhanced by visual feedback. Recently, technical advances have made it possible also to investigate more complex, realistic motor tasks and to implement not only visual, but also auditory, haptic, or multimodal augmented feedback. The aim of this review is to address the potential of augmented unimodal and multimodal feedback in the framework of motor learning theories. The review addresses the reasons for the different impacts of feedback strategies within or between the visual, auditory, and haptic modalities and the challenges that need to be overcome to provide appropriate feedback in these modalities, either in isolation or in combination. Accordingly, the design criteria for successful visual, auditory, haptic, and multimodal feedback are elaborated.''', 
    tags = [education, audio_visual_haptic], 
    my_notes = r'''
Identifies AVH.  
Good paper to go back to. (And when you do, take notes this time.)  
''', 
)

instructional_design_and_intelligent_tutoring_theory_and_the_precision_of_design = Paper(
    apa = r'''Capell, P., & Dannenberg, R. B. (1993). Instructional design and intelligent tutoring: Theory and the precision of design.''', 
    bib = r'''@article{capell1993instructional,
  title={Instructional design and intelligent tutoring: Theory and the precision of design},
  author={Capell, Peter and Dannenberg, Roger B},
  year={1993},
  publisher={Carnegie Mellon University}
}''', 
    abstract = r'''Instructional Design aspires to define a sound curriculum by using instructional analysis and concept organization. Along with other criteria, the purpose of instructional design is to ensure integrity among instructional objectives, tasks that students must perform, and the evaluation of their performance. Currently, the methods used in instructional design models have a limited scientific basis. Even with many efforts towards a science of instruction, this goal remains elusive. Computers may provide a positive shift towards systematic and verifiable instructional analysis with the advent of intelligent tutoring systems and the byproducts of their development. One such system, the Piano Tutor, has led to a formal model for curriculum design and analysis and is described in detail.''', 
    tags = [education], 
    my_notes = r'''
Skill & lesson graph. Formal analysis.  
''', 
)

an_expert_system_for_teaching_piano_to_novices = Paper(
    apa = r'''Dannenberg, R. B., Sanchez, M., Joseph, A., Capell, P., Joseph, R., & Saul, R. (1990). An expert system for teaching piano to novices. In ICMC.''', 
    bib = r'''@inproceedings{dannenberg1990expert,
  title={An expert system for teaching piano to novices},
  author={Dannenberg, Roger B and Sanchez, Marta and Joseph, Annabel and Capell, Peter and Joseph, Robert and Saul, Ronald},
  booktitle={ICMC},
  year={1990}
}''', 
    abstract = r'''The Piano Tutor is a computer system for teaching beginning piano students. The system is highly interactive, with an expert system to analyze student performances and a multi-media presentation system to deliver instruction. Score following, which matches performances against a model, is used as the basis for detecting student errors. The Piano Tutor gives intelligent feedback and help rather than just listing all errors that are detected. The curriculum is organized into a set of lessons that are automatically chosen by the system according to students' needs.''', 
    tags = [education, multimodal], 
    my_notes = r'''
Piano Tutor can hypothesize the cause behind a student error.  
''', 
)

a_computer_based_multi_media_tutor_for_beginning_piano_students = Paper(
    apa = r'''Dannenberg, R. B., Sanchez, M., Joseph, A., Capell, P., Joseph, R., & Saul, R. (1990). A computer‐based multi‐media tutor for beginning piano students. Journal of New Music Research, 19(2-3), 155-173.''', 
    bib = r'''@article{dannenberg1990computer,
  title={A computer-based multi-media tutor for beginning piano students},
  author={Dannenberg, Roger B and Sanchez, Marta and Joseph, Annabelle and Capell, Peter and Joseph, Robert and Saul, Ronald},
  journal={Journal of New Music Research},
  volume={19},
  number={2-3},
  pages={155--173},
  year={1990},
  publisher={Taylor \& Francis}
}''', 
    abstract = r'''The Piano Tutor provides computer‐based instruction to beginning piano students. Intended as a supplement to traditional instruction, the Piano Tutor helps students by correcting mistakes before they become ingrained through practice and by teaching new material as soon as the student is ready. The Piano Tutor combines an expert system with state‐of‐the‐art music recognition software and multimedia output devices to provide a stimulating learning environment that tailors instruction to the student's needs.''', 
    tags = [education, multimodal], 
)

visual_chatgpt_talking_drawing_and_editing_with_visual_foundation_models = Paper(
    shorts = ['Visual ChatGPT'],
    apa = r'''Wu, C., Yin, S., Qi, W., Wang, X., Tang, Z., & Duan, N. (2023). Visual chatgpt: Talking, drawing and editing with visual foundation models. arXiv preprint arXiv:2303.04671.''', 
    bib = r'''@article{wu2023visual,
  title={Visual chatgpt: Talking, drawing and editing with visual foundation models},
  author={Wu, Chenfei and Yin, Shengming and Qi, Weizhen and Wang, Xiaodong and Tang, Zecheng and Duan, Nan},
  journal={arXiv preprint arXiv:2303.04671},
  year={2023}
}''', 
    abstract = r'''ChatGPT is attracting a cross-field interest as it provides a language interface with remarkable conversational competency and reasoning capabilities across many domains. However, since ChatGPT is trained with languages, it is currently not capable of processing or generating images from the visual world. At the same time, Visual Foundation Models, such as Visual Transformers or Stable Diffusion, although showing great visual understanding and generation capabilities, they are only experts on specific tasks with one-round fixed inputs and outputs. To this end, We build a system called 	extbf{Visual ChatGPT}, incorporating different Visual Foundation Models, to enable the user to interact with ChatGPT by 1) sending and receiving not only languages but also images 2) providing complex visual questions or visual editing instructions that require the collaboration of multiple AI models with multi-steps. 3) providing feedback and asking for corrected results. We design a series of prompts to inject the visual model information into ChatGPT, considering models of multiple inputs/outputs and models that require visual feedback. Experiments show that Visual ChatGPT opens the door to investigating the visual roles of ChatGPT with the help of Visual Foundation Models. Our system is publicly available at https://github.com/microsoft/visual-chatgpt.''', 
    tags = [llm, llm_in_the_loop], 
)

the_learning_of_90_continuous_relative_phase_with_and_without_lissajous_feedback_external_and_internally_generated_bimanual_coordination = Paper(
    apa = r'''Kovacs, A. J., & Shea, C. H. (2011). The learning of 90 continuous relative phase with and without Lissajous feedback: external and internally generated bimanual coordination. Acta psychologica, 136(3), 311-320.''', 
    bib = r'''@article{kovacs2011learning,
  title={The learning of 90 continuous relative phase with and without Lissajous feedback: external and internally generated bimanual coordination},
  author={Kovacs, Attila J and Shea, Charles H},
  journal={Acta psychologica},
  volume={136},
  number={3},
  pages={311--320},
  year={2011},
  publisher={Elsevier}
}''', 
    abstract = r'''Results from recent experiments (e.g., Kovacs, Buchanan, & Shea, 2009a–b, 2010a,b) suggest that when salient visual information is presented using Lissajous plots bimanual coordination patterns typically thought to be very difficult to perform without extensive practice can be performed with remarkably low relative phase error and variability with 5 min or less of practice. However, when this feedback is removed, performance deteriorates. The purpose of the present experiment was to determine if reducing the frequency of feedback presentation will decrease the participant's reliance on the feedback and will facilitate the development of an internal representation capable of sustaining performance when the Lissajous feedback is withdrawn. The results demonstrated that reduced frequency Lissajous feedback results in very effective bimanual coordination performance on tests with Lissajous feedback available and when feedback is withdrawn. Taken together the present experiments add to the growing literature that supports the notion that salient perceptual information can override some aspects of the system's intrinsic dynamics typically linked to motor output control. Additionally, the present results suggest that the learning of both externally and internally driven bimanual coordination is facilitated by providing reduced frequency Lissajous feedback.''', 
    tags = [], 
    my_notes = r'''
Reduce feedback frequency over time.  
"For a block of 10 trials feedback presentation
under the fading schedule was presented as follows: 25–25–20–20–
15–15–10–10–5–5 s for each consecutive trial. The feedback was
provided at the beginning of each trial and withdrawn according to
the schedule above."
''', 
)

performance_on_trials_without_knowledge_of_results_kr_in_reduced_relative_frequency_presentations_of_kr = Paper(
    apa = r'''Sparrow, W. A., & Summers, J. J. (1992). Performance on trials without knowledge of results (KR) in reduced relative frequency presentations of KR. Journal of motor behavior, 24(2), 197-209.''', 
    bib = r'''@article{sparrow1992performance,
  title={Performance on trials without knowledge of results (KR) in reduced relative frequency presentations of KR},
  author={Sparrow, Wl A and Summers, JJ},
  journal={Journal of motor behavior},
  volume={24},
  number={2},
  pages={197--209},
  year={1992},
  publisher={Taylor \& Francis}
}''', 
    abstract = r'''Following Salmoni, Schmidt, & Walter's (1984) discussion of knowledge of results (KR) as a variable influencing learning, the effect of varying relative frequency of KR while holding absolute number of trials constant was examined. In two experiments, the same treatment groups were compared in acquisition, retention (after 2 min and 24 hr), and on their pattern of responses on the sequence of no-KR trials following a KR trial. In Experiment 1, differences between groups in acquisition were consistent with the number of KR trials received, and there were no differences between groups in either of the retention conditions. Experiment 2 replicated Experiment 1 with a more difficult task. There were no between-group differences in acquisition. In Retention 1, the 100% and 33% relative frequency groups outperformed the less frequent KR groups, whereas in Retention 2, this trend was reversed. The findings from Experiment 2 provide qualified support for the hypothesis that reduced relative frequency of KR in acquisition facilitates performance in retention. The pattern of responses on the sequence of no-KR trials following a KR trial were consistent with Adams' (1971) perceptual-trace decay hypothesis.''', 
    tags = [education, adaptive_curriculum_scaffolding], 
)

bert_pre_training_of_deep_bidirectional_transformers_for_language_understanding = Paper(
    apa = r'''Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805.''', 
    bib = r'''@article{devlin2018bert,
  title={Bert: Pre-training of deep bidirectional transformers for language understanding},
  author={Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  journal={arXiv preprint arXiv:1810.04805},
  year={2018}
}''', 
    abstract = r'''We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.
BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).''', 
    tags = [lm], 
)

auto_encoding_variational_bayes = Paper(
    apa = r'''Kingma, D. P., & Welling, M. (2013). Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114.''', 
    bib = r'''@article{kingma2013auto,
  title={Auto-encoding variational bayes},
  author={Kingma, Diederik P and Welling, Max},
  journal={arXiv preprint arXiv:1312.6114},
  year={2013}
}''', 
    abstract = r'''How can we perform efficient inference and learning in directed probabilistic models, in the presence of continuous latent variables with intractable posterior distributions, and large datasets? We introduce a stochastic variational inference and learning algorithm that scales to large datasets and, under some mild differentiability conditions, even works in the intractable case. Our contributions are two-fold. First, we show that a reparameterization of the variational lower bound yields a lower bound estimator that can be straightforwardly optimized using standard stochastic gradient methods. Second, we show that for i.i.d. datasets with continuous latent variables per datapoint, posterior inference can be made especially efficient by fitting an approximate inference model (also called a recognition model) to the intractable posterior using the proposed lower bound estimator. Theoretical advantages are reflected in experimental results.''', 
    tags = [], 
    my_notes = r'''vae''', 
)

a_recurrent_latent_variable_model_for_sequential_data = Paper(
    apa = r'''Chung, J., Kastner, K., Dinh, L., Goel, K., Courville, A. C., & Bengio, Y. (2015). A recurrent latent variable model for sequential data. Advances in neural information processing systems, 28.''', 
    bib = r'''@article{chung2015recurrent,
  title={A recurrent latent variable model for sequential data},
  author={Chung, Junyoung and Kastner, Kyle and Dinh, Laurent and Goel, Kratarth and Courville, Aaron C and Bengio, Yoshua},
  journal={Advances in neural information processing systems},
  volume={28},
  year={2015}
}''', 
    abstract = r'''In this paper, we explore the inclusion of latent random variables into the hidden state of a recurrent neural network (RNN) by combining the elements of the variational autoencoder. We argue that through the use of high-level latent random variables, the variational RNN (VRNN) can model the kind of variability observed in highly structured sequential data such as natural speech. We empirically evaluate the proposed model against other related sequential models on four speech datasets and one handwriting dataset. Our results show the important roles that latent random variables can play in the RNN dynamics.''', 
    tags = [], 
    my_notes = r'''vrnn''', 
)

deep_symmetry_networks = Paper(
    apa = r'''Gens, R., & Domingos, P. M. (2014). Deep symmetry networks. Advances in neural information processing systems, 27.''', 
    bib = r'''@article{gens2014deep,
  title={Deep symmetry networks},
  author={Gens, Robert and Domingos, Pedro M},
  journal={Advances in neural information processing systems},
  volume={27},
  year={2014}
}''', 
    abstract = r'''The chief difficulty in object recognition is that objects’ classes are obscured by a large number of extraneous sources of variability, such as pose and part deformation. These sources of variation can be represented by symmetry groups, sets of composable transformations that preserve object identity. Convolutional neural networks (convnets) achieve a degree of translational invariance by computing feature maps over the translation group, but cannot handle other groups. As a result, these groups’ effects have to be approximated by small translations, which often requires augmenting datasets and leads to high sample complexity. In this paper, we introduce deep symmetry networks (symnets), a generalization of convnets that forms feature maps over arbitrary symmetry groups. Symnets use kernel-based interpolation to tractably tie parameters and pool over symmetry spaces of any dimension. Like convnets, they are trained with backpropagation. The composition of feature transformations through the layers of a symnet provides a new approach to deep learning. Experiments on NORB and MNIST-rot show that symnets over the affine group greatly reduce sample complexity relative to convnets by better capturing the symmetries in the data.''', 
    tags = [symmetry], 
)

group_equivariant_convolutional_networks = Paper(
    apa = r'''Cohen, T., & Welling, M. (2016, June). Group equivariant convolutional networks. In International conference on machine learning (pp. 2990-2999). PMLR.''', 
    bib = r'''@inproceedings{cohen2016group,
  title={Group equivariant convolutional networks},
  author={Cohen, Taco and Welling, Max},
  booktitle={International conference on machine learning},
  pages={2990--2999},
  year={2016},
  organization={PMLR}
}''', 
    abstract = r'''We introduce Group equivariant Convolutional Neural Networks (G-CNNs), a natural generalization of convolutional neural networks that reduces sample complexity by exploiting symmetries. G-CNNs use G-convolutions, a new type of layer that enjoys a substantially higher degree of weight sharing than regular convolution layers. G-convolutions increase the expressive capacity of the network without increasing the number of parameters. Group convolution layers are easy to use and can be implemented with negligible computational overhead for discrete groups generated by translations, reflections and rotations. G-CNNs achieve state of the art results on CIFAR10 and rotated MNIST.''', 
    tags = [symmetry, repr_learning], 
)

perceiver_general_perception_with_iterative_attention = Paper(
    apa = r'''Jaegle, A., Gimeno, F., Brock, A., Vinyals, O., Zisserman, A., & Carreira, J. (2021, July). Perceiver: General perception with iterative attention. In International conference on machine learning (pp. 4651-4664). PMLR.''', 
    bib = r'''@inproceedings{jaegle2021perceiver,
  title={Perceiver: General perception with iterative attention},
  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andy and Vinyals, Oriol and Zisserman, Andrew and Carreira, Joao},
  booktitle={International conference on machine learning},
  pages={4651--4664},
  year={2021},
  organization={PMLR}
}''', 
    abstract = r'''Biological systems understand the world by simultaneously processing high-dimensional inputs from modalities as diverse as vision, audition, touch, proprioception, etc. The perception models used in deep learning on the other hand are designed for individual modalities, often relying on domain-specific assumptions such as the local grid structures exploited by virtually all existing vision models. These priors introduce helpful inductive biases, but also lock models to individual modalities. In this paper we introduce the Perceiver {–} a model that builds upon Transformers and hence makes few architectural assumptions about the relationship between its inputs, but that also scales to hundreds of thousands of inputs, like ConvNets. The model leverages an asymmetric attention mechanism to iteratively distill inputs into a tight latent bottleneck, allowing it to scale to handle very large inputs. We show that this architecture is competitive with or outperforms strong, specialized models on classification tasks across various modalities: images, point clouds, audio, video and video+audio. The Perceiver obtains performance comparable to ResNet-50 and ViT on ImageNet without 2D convolutions by directly attending to 50,000 pixels. It is also competitive in all modalities in AudioSet.''', 
    tags = [], 
)

emergent_world_representations_exploring_a_sequence_model_trained_on_a_synthetic_task = Paper(
    apa = r'''Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2022). Emergent world representations: Exploring a sequence model trained on a synthetic task. arXiv preprint arXiv:2210.13382.''', 
    bib = r'''@article{li2022emergent,
  title={Emergent world representations: Exploring a sequence model trained on a synthetic task},
  author={Li, Kenneth and Hopkins, Aspen K and Bau, David and Vi{\'e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
  journal={arXiv preprint arXiv:2210.13382},
  year={2022}
}''', 
    abstract = r'''Language models show a surprising range of capabilities, but the source of their apparent competence is unclear. Do these networks just memorize a collection of surface statistics, or do they rely on internal representations of the process that generates the sequences they see? We investigate this question by applying a variant of the GPT model to the task of predicting legal moves in a simple board game, Othello. Although the network has no a priori knowledge of the game or its rules, we uncover evidence of an emergent nonlinear internal representation of the board state. Interventional experiments indicate this representation can be used to control the output of the network and create "latent saliency maps" that can help explain predictions in human terms.''', 
    tags = [emergent_symbols], 
    my_notes = r'''
Good.  
The world state is highly probe-able.  
The probe is so nice you can use its gradients to  
    - analyze saliency  
    - intervene predictions.  
My ideas:
    - Probe-ability says something about 
(existence of repr \intersect quality of repr). I believe the existence of repr is always true. Probe-ability usually evaluates repr quality. 
    - Symm's number experiment cannot use this method because probe-ability is also determined by probing task complexity. Forming a bijective map of 15 elements is too trivial. Poor-quality repr can be probe-able.  
Questions:
    - Why call transformer "GPT"?  
''', 
)

deep_symbolic_learning_discovering_symbols_and_rules_from_perceptions = Paper(
    apa = r'''Daniele, A., Campari, T., Malhotra, S., & Serafini, L. (2022). Deep symbolic learning: Discovering symbols and rules from perceptions. arXiv preprint arXiv:2208.11561.''', 
    bib = r'''@article{daniele2022deep,
  title={Deep symbolic learning: Discovering symbols and rules from perceptions},
  author={Daniele, Alessandro and Campari, Tommaso and Malhotra, Sagar and Serafini, Luciano},
  journal={arXiv preprint arXiv:2208.11561},
  year={2022}
}''', 
    abstract = r'''Neuro-Symbolic (NeSy) integration combines symbolic reasoning with Neural Networks (NNs) for tasks requiring perception and reasoning. Most NeSy systems rely on continuous relaxation of logical knowledge, and no discrete decisions are made within the model pipeline. Furthermore, these methods assume that the symbolic rules are given. In this paper, we propose Deep Symbolic Learning (DSL), a NeSy system that learns NeSy-functions, i.e., the composition of a (set of) perception functions which map continuous data to discrete symbols, and a symbolic function over the set of symbols. DSL learns simultaneously the perception and symbolic functions while being trained only on their composition (NeSy-function). The key novelty of DSL is that it can create internal (interpretable) symbolic representations and map them to perception inputs within a differentiable NN learning pipeline. The created symbols are automatically selected to generate symbolic functions that best explain the data. We provide experimental analysis to substantiate the efficacy of DSL in simultaneously learning perception and symbolic functions.''', 
    tags = [emergent_symbols], 
    my_notes = r'''
Too trivial?  
''', 
)

understanding_the_challenges_for_adult_beginners_at_piano_practice_from_an_analysis_of_errors = Paper(
    apa = None, 
    bib = None, 
    abstract = r'''Adult beginners at piano playing tend to have positive characteristics related to learning, such as being analytical, goal-oriented, and attentive. While some adult beginners face the need to acquire performance skills, for example, in teacher training, some people learn to play the piano just as a hobby. From an educational standpoint, it is important to understand the tendencies of their errors in playing and how these errors can be reduced over time with practice. 
The purpose of this research was to investigate the types of errors that adult beginners at piano playing experienced during their practice time and how they improved their performance. Eight adults (M = 6, F=2; mean age = 42.5 years), who were beginners at keyboard playing, participated in an experimental study. All the participants were given a sheet, with music newly composed for this study, and asked to practice it for three minutes on an electric piano(Yamaha Digital Piano P-125) after watching a demo. After the three-minute practice, each participant was asked to perform the piece once from the beginning to the end. A set of three minutes of practice followed by a performance was repeated five times. After all sessions,each participant took part in a semi-structured interview. All performance data, including practices, were recorded with two cameras set at different angles, and exported as MIDI audiodata. Audio and video data were analyzed and the errors identified were categorized into three types: beat interruption, rhythm errors, and pitch errors. 
The data revealed that errors of beat interruption were most frequent among all types of errors and remained up to the final stage of practice. The distribution of decreased errors was not always linear, but was highly likely to be graphically presented as a zig-zag line with over adaptation and self-regulated processes. The interview data indicated that adult learners had different strategies and priorities for playing. The results showed that some new processes learned could temporally interfere with other parts of playing, and a certain amount of time is needed to assimilate what they achieved. The study also suggested that understanding the learners’ individual needs during their practices could be crucial, as well as support for practice strategies.''', 
    tags = [education], 
    my_notes = r'''
Three kinds of error: pause, rhythm error, pitch error.
''', 
)

gait_retraining_to_reduce_lower_extremity_loading_in_runners = Paper(
    apa = r'''Crowell, H. P., & Davis, I. S. (2011). Gait retraining to reduce lower extremity loading in runners. Clinical biomechanics, 26(1), 78-83.''', 
    bib = r'''@article{crowell2011gait,
  title={Gait retraining to reduce lower extremity loading in runners},
  author={Crowell, Harrison Philip and Davis, Irene S},
  journal={Clinical biomechanics},
  volume={26},
  number={1},
  pages={78--83},
  year={2011},
  publisher={Elsevier}
}''', 
    abstract = r'''Background
Tibial stress fractures, which are among the most common running related injuries, have been associated with increased lower extremity loading (i.e., peak positive acceleration of the tibia, vertical force impact peak, and average and instantaneous vertical force loading rates) during initial contact. This study was conducted to evaluate the efficacy of a gait retraining program designed to reduce this loading during running and to assess the short-term persistence of these reductions.

Methods
Ten runners (six females and four males) with peak positive tibial acceleration greater than 8 g, measured in an initial screening, participated in the retraining program. During the retraining sessions, subjects ran on a treadmill and received real-time visual feedback from an accelerometer attached to their distal tibias. Tibial acceleration and vertical ground reaction force data were collected from subjects during overground data collection sessions held pre-training, post-training, and at a 1-month follow-up.

Findings
Peak positive acceleration of the tibia, vertical force impact peak, and average and instantaneous vertical force loading rates were all reduced immediately following the gait retraining. The decrease in tibial acceleration was nearly 50%. The reductions in vertical force loading rates and vertical force impact peak were approximately 30% and 20%, respectively. These reductions were maintained at the 1-month follow-up.

Interpretation
Subjects were able to run with reduced tibial acceleration and vertical force loading immediately following completion of the gait retraining program and at the 1-month follow-up evaluation. This may reduce their risk of stress fractures.
''', 
    tags = [education, adaptive_curriculum_scaffolding], 
    my_notes = r'''''', 
)

gacela_a_generative_adversarial_context_encoder_for_long_audio_inpainting_of_music = Paper(
    apa = r'''Marafioti, A., Majdak, P., Holighaus, N., & Perraudin, N. (2020). GACELA: A generative adversarial context encoder for long audio inpainting of music. IEEE Journal of Selected Topics in Signal Processing, 15(1), 120-131.''', 
    bib = r'''@article{marafioti2020gacela,
  title={GACELA: A generative adversarial context encoder for long audio inpainting of music},
  author={Marafioti, Andres and Majdak, Piotr and Holighaus, Nicki and Perraudin, Nathana{\"e}l},
  journal={IEEE Journal of Selected Topics in Signal Processing},
  volume={15},
  number={1},
  pages={120--131},
  year={2020},
  publisher={IEEE}
}''', 
    abstract = r'''In this article, we introduce GACELA, a conditional generative adversarial network (cGAN) designed to restore missing audio data with durations ranging between hundreds of milliseconds and a few seconds, i.e., to perform long-gap audio inpainting. While previous work either addressed shorter gaps or relied on exemplars by copying available information from other signal parts, GACELA addresses the inpainting of long gaps in two aspects. First, it considers various time scales of audio information by relying on five parallel discriminators with increasing resolution of receptive fields. Second, it is conditioned not only on the available information surrounding the gap, i.e., the context, but also on the latent variable of the cGAN. This addresses the inherent multi-modality of audio inpainting for such long gaps while providing the user with different inpainting options. GACELA was evaluated in listening tests on music signals of varying complexity and varying gap durations from 375 to 1500 ms. Under laboratory conditions, our subjects were often able to detect the inpainting. However, the severity of the inpainted artifacts was rated between not disturbing and mildly disturbing. GACELA represents a framework capable of integrating future improvements such as processing of more auditory-related features or explicit musical features. Our software and trained models, complemented by instructive examples, are available online.''', 
    tags = [inpaint, music_audio, lit_review_for_liwei_ijcai_2024], 
)

vision_infused_deep_audio_inpainting = Paper(
    apa = r'''Zhou, H., Liu, Z., Xu, X., Luo, P., & Wang, X. (2019). Vision-infused deep audio inpainting. In Proceedings of the IEEE/CVF International Conference on Computer Vision (pp. 283-292).''', 
    bib = r'''@inproceedings{zhou2019vision,
  title={Vision-infused deep audio inpainting},
  author={Zhou, Hang and Liu, Ziwei and Xu, Xudong and Luo, Ping and Wang, Xiaogang},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={283--292},
  year={2019}
}''', 
    abstract = r'''Multi-modality perception is essential to develop interactive intelligence. In this work, we consider a new task of visual information-infused audio inpainting, i.e., synthesizing missing audio segments that correspond to their accompanying videos. We identify two key aspects for a successful inpainter: (1) It is desirable to operate on spectrograms instead of raw audios. Recent advances in deep semantic image inpainting could be leveraged to go beyond the limitations of traditional audio inpainting. (2) To synthesize visually indicated audio, a visual-audio joint feature space needs to be learned with synchronization of audio and video. To facilitate a large-scale study, we collect a new multi-modality instrument-playing dataset called MUSIC-Extra-Solo (MUSICES) by enriching MUSIC dataset. Extensive experiments demonstrate that our framework is capable of inpainting realistic and varying audio segments with or without visual contexts. More importantly, our synthesized audio segments are coherent with their video counterparts, showing the effectiveness of our proposed Vision-Infused Audio Inpainter (VIAI).''', 
    tags = [inpaint, music_audio, lit_review_for_liwei_ijcai_2024], 
)

the_piano_inpainting_application = Paper(
    apa = r'''Hadjeres, G., & Crestel, L. (2021). The piano inpainting application. arXiv preprint arXiv:2107.05944.''', 
    bib = r'''@article{hadjeres2021piano,
  title={The piano inpainting application},
  author={Hadjeres, Ga{\"e}tan and Crestel, L{\'e}opold},
  journal={arXiv preprint arXiv:2107.05944},
  year={2021}
}''', 
    abstract = r'''Autoregressive models are now capable of generating high-quality minute-long expressive MIDI piano performances. Even though this progress suggests new tools to assist music composition, we observe that generative algorithms are still not widely used by artists due to the limited control they offer, prohibitive inference times or the lack of integration within musicians' workflows. In this work, we present the Piano Inpainting Application (PIA), a generative model focused on inpainting piano performances, as we believe that this elementary operation (restoring missing parts of a piano performance) encourages human-machine interaction and opens up new ways to approach music composition. Our approach relies on an encoder-decoder Linear Transformer architecture trained on a novel representation for MIDI piano performances termed Structured MIDI Encoding. By uncovering an interesting synergy between Linear Transformers and our inpainting task, we are able to efficiently inpaint contiguous regions of a piano performance, which makes our model suitable for interactive and responsive A.I.-assisted composition. Finally, we introduce our freely-available Ableton Live PIA plugin, which allows musicians to smoothly generate or modify any MIDI clip using PIA within a widely-used professional Digital Audio Workstation.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024], 
    my_notes = r'''
Cannot find inpainting demo.  
''', 
)

music_sketchnet_controllable_music_generation_via_factorized_representations_of_pitch_and_rhythm = Paper(
    shorts = ['Music sketchnet'], 
    apa = r'''Chen, K., Wang, C. I., Berg-Kirkpatrick, T., & Dubnov, S. (2020). Music sketchnet: Controllable music generation via factorized representations of pitch and rhythm. In Ismir 2020 Conference.''', 
    bib = r'''@inproceedings{chen2020music,
  title={Music sketchnet: Controllable music generation via factorized representations of pitch and rhythm},
  author={Chen, Ke and Wang, Cheng-i and Berg-Kirkpatrick, Taylor and Dubnov, Shlomo},
  booktitle={Ismir 2020 Conference},
  year={2020}
}''', 
    abstract = r'''Drawing an analogy with automatic image completion systems, we propose Music SketchNet, a neural network framework that allows users to specify partial musical ideas guiding automatic music generation. We focus on generating the missing measures in incomplete monophonic musical pieces, conditioned on surrounding context, and optionally guided by user-specified pitch and rhythm snippets. First, we introduce SketchVAE, a novel variational autoencoder that explicitly factorizes rhythm and pitch contour to form the basis of our proposed model. Then we introduce two discriminative architectures, SketchInpainter and SketchConnector, that in conjunction perform the guided music completion, filling in representations for the missing measures conditioned on surrounding context and user-specified snippets. We evaluate SketchNet on a standard dataset of Irish folk music and compare with models from recent works. When used for music completion, our approach outperforms the state-of-the-art both in terms of objective metrics and subjective listening tests. Finally, we demonstrate that our model can successfully incorporate user-specified snippets during the generation process.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024], 
)

vampnet_music_generation_via_masked_acoustic_token_modeling = Paper(
    shorts = ['Vampnet'], 
    apa = r'''Garcia, H. F. F., Seetharaman, P., Kumar, R., & Pardo, B. (2023, November). VampNet: Music Generation via Masked Acoustic Token Modeling. In Ismir 2023 Hybrid Conference.''', 
    bib = r'''@inproceedings{garcia2023vampnet,
  title={VampNet: Music Generation via Masked Acoustic Token Modeling},
  author={Garcia, Hugo F Flores and Seetharaman, Prem and Kumar, Rithesh and Pardo, Bryan},
  booktitle={Ismir 2023 Hybrid Conference},
  year={2023}
}''', 
    abstract = r'''We introduce VampNet, a masked acoustic token modeling approach to music synthesis, compression, inpainting, and variation. We use a variable masking schedule during training which allows us to sample coherent music from the model by applying a variety of masking approaches (called prompts) during inference. VampNet is non-autoregressive, leveraging a bidirectional transformer architecture that attends to all tokens in a forward pass. With just 36 sampling passes, VampNet can generate coherent high-fidelity musical waveforms. We show that by prompting VampNet in various ways, we can apply it to tasks like music compression, inpainting, outpainting, continuation, and looping with variation (vamping). Appropriately prompted, VampNet is capable of maintaining style, genre, instrumentation, and other high-level aspects of the music. This flexible prompting capability makes VampNet a powerful music co-creation tool. Code and audio samples are available online.''', 
    tags = [inpaint, music_audio, lit_review_for_liwei_ijcai_2024], 
    my_notes = r'''
Direct MLM.  
1 or 2 sec inpaint.  
''', 
)

musiac_an_extensible_generative_framework_for_music_infilling_applications_with_multi_level_control = Paper(
    apa = r'''Guo, R., Simpson, I., Kiefer, C., Magnusson, T., & Herremans, D. (2022, April). MusIAC: An extensible generative framework for Music Infilling Applications with multi-level Control. In International Conference on Computational Intelligence in Music, Sound, Art and Design (Part of EvoStar) (pp. 341-356). Cham: Springer International Publishing.''', 
    bib = r'''@inproceedings{guo2022musiac,
  title={MusIAC: An extensible generative framework for Music Infilling Applications with multi-level Control},
  author={Guo, Rui and Simpson, Ivor and Kiefer, Chris and Magnusson, Thor and Herremans, Dorien},
  booktitle={International Conference on Computational Intelligence in Music, Sound, Art and Design (Part of EvoStar)},
  pages={341--356},
  year={2022},
  organization={Springer}
}''', 
    abstract = r'''We present a novel music generation framework for music infilling, with a user friendly interface. Infilling refers to the task of generating musical sections given the surrounding multi-track music. The proposed transformer-based framework is extensible for new control tokens as the added music control tokens such as tonal tension per bar and track polyphony level in this work. We explore the effects of including several musically meaningful control tokens, and evaluate the results using objective metrics related to pitch and rhythm. Our results demonstrate that adding additional control tokens helps to generate music with stronger stylistic similarities to the original music. It also provides the user with more control to change properties like the music texture and tonal tension in each bar compared to previous research which only provided control for track density. We present the model in a Google Colab notebook to enable interactive generation.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024], 
    my_notes = r'''
direct MLM.  
1-bar inpaint.  
two-stage training: first short masks then long masks.  
''', 
)

variable_length_music_score_infilling_via_xlnet_and_musically_specialized_positional_encoding = Paper(
    apa = r'''Chang, C. J., Lee, C. Y., & Yang, Y. H. (2021). Variable-length music score infilling via XLNet and musically specialized positional encoding. In Ismir 2021 Conference.''', 
    bib = r'''@inproceedings{chang2021variable,
  title={Variable-length music score infilling via XLNet and musically specialized positional encoding},
  author={Chang, Chin-Jui and Lee, Chun-Yi and Yang, Yi-Hsuan},
  booktitle={Ismir 2021 Conference},
  year={2021}
}''', 
    abstract = r'''This paper proposes a new self-attention based model for music score infilling, i.e., to generate a polyphonic music sequence that fills in the gap between given past and future contexts. While existing approaches can only fill in a short segment with a fixed number of notes, or a fixed time span between the past and future contexts, our model can infill a variable number of notes (up to 128) for different time spans. We achieve so with three major technical contributions. First, we adapt XLNet, an autoregressive model originally proposed for unsupervised model pre-training, to music score infilling. Second, we propose a new, musically specialized positional encoding called relative bar encoding that better informs the model of notes' position within the past and future context. Third, to capitalize relative bar encoding, we perform look-ahead onset prediction to predict the onset of a note one time step before predicting the other attributes of the note. We compare our proposed model with two strong baselines and show that our model is superior in both objective and subjective analyses.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024], 
)

infilling_piano_performances = Paper(
    apa = r'''Ippolito, D., Huang, A., Hawthorne, C., & Eck, D. (2018). Infilling piano performances. In NIPS Workshop on Machine Learning for Creativity and Design (Vol. 2, p. 5).''', 
    bib = r'''@inproceedings{ippolito2018infilling,
  title={Infilling piano performances},
  author={Ippolito, Daphne and Huang, Anna and Hawthorne, Curtis and Eck, Douglas},
  booktitle={NIPS Workshop on Machine Learning for Creativity and Design},
  volume={2},
  pages={5},
  year={2018}
}''', 
    abstract = r'''Existing systems for music generation have generated music in a left-to-right direction or have used a fill-in-the-blank approach on a quantized piano-roll musical representation. In this work, we show that it is possible to train a self-attention based Transformer to infill deleted sections of MIDI transcriptions of performed piano music. This infilling technique can be used collaboratively by composers to select contiguous sections of their work to be ‘rewritten’ by a neural net. It can also be used to gradually morph one musical piece into a different one.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024], 
    my_notes = r'''
Prefix; suffix; continuation.  
Inpainting via reordering. MLM via auto-regressive LM.  
''', 
)

polyffusion_a_diffusion_model_for_polyphonic_score_generation_with_internal_and_external_controls = Paper(
    apa = r'''Min, L., Jiang, J., Xia, G., & Zhao, J. (2023, November). Polyffusion: A Diffusion Model for Polyphonic Score Generation With Internal and External Controls. In Ismir 2023 Hybrid Conference.''', 
    bib = r'''@inproceedings{min2023polyffusion,
  title={Polyffusion: A Diffusion Model for Polyphonic Score Generation With Internal and External Controls},
  author={Min, Lejun and Jiang, Junyan and Xia, Gus and Zhao, Jingwei},
  booktitle={Ismir 2023 Hybrid Conference},
  year={2023}
}''', 
    abstract = r'''We propose Polyffusion, a diffusion model that generates polyphonic music scores by regarding music as image-like piano roll representations. The model is capable of controllable music generation with two paradigms: internal control and external control. Internal control refers to the process in which users pre-define a part of the music and then let the model infill the rest, similar to the task of masked music generation (or music inpainting). External control conditions the model with external yet related information, such as chord, texture, or other features, via the cross-attention mechanism. We show that by using internal and external controls, Polyffusion unifies a wide range of music creation tasks, including melody generation given accompaniment, accompaniment generation given melody, arbitrary music segment inpainting, and music arrangement given chords or textures. Experimental results show that our model significantly outperforms existing Transformer and sampling-based baselines, and using pre-trained disentangled representations as external conditions yields more effective controls.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024, diffusion], 
)

counterpoint_by_convolution = Paper(
    shorts = ['Coconet'], 
    apa = r'''Huang, C. Z. A., Cooijmans, T., Roberts, A., Courville, A., & Eck, D. (2019). Counterpoint by convolution. arXiv preprint arXiv:1903.07227.''', 
    bib = r'''@article{huang2019counterpoint,
  title={Counterpoint by convolution},
  author={Huang, Cheng-Zhi Anna and Cooijmans, Tim and Roberts, Adam and Courville, Aaron and Eck, Douglas},
  journal={arXiv preprint arXiv:1903.07227},
  year={2019}
}''', 
    abstract = r'''Machine learning models of music typically break up the task of composition into a chronological process, composing a piece of music in a single pass from beginning to end. On the contrary, human composers write music in a nonlinear fashion, scribbling motifs here and there, often revisiting choices previously made. In order to better approximate this process, we train a convolutional neural network to complete partial musical scores, and explore the use of blocked Gibbs sampling as an analogue to rewriting. Neither the model nor the generative procedure are tied to a particular causal direction of composition. Our model is an instance of orderless NADE (Uria et al., 2014), which allows more direct ancestral sampling. However, we find that Gibbs sampling greatly improves sample quality, which we demonstrate to be due to some conditional distributions being poorly modeled. Moreover, we show that even the cheap approximate blocked Gibbs procedure from Yao et al. (2014) yields better samples than ancestral sampling, based on both log-likelihood and human evaluation.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024], 
)

a_context_encoder_for_audio_inpainting = Paper(
    apa = r'''Marafioti, A., Perraudin, N., Holighaus, N., & Majdak, P. (2019). A context encoder for audio inpainting. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 27(12), 2362-2372.''', 
    bib = r'''@article{marafioti2019context,
  title={A context encoder for audio inpainting},
  author={Marafioti, Andr{\'e}s and Perraudin, Nathana{\"e}l and Holighaus, Nicki and Majdak, Piotr},
  journal={IEEE/ACM Transactions on Audio, Speech, and Language Processing},
  volume={27},
  number={12},
  pages={2362--2372},
  year={2019},
  publisher={IEEE}
}''', 
    abstract = r'''In this article, we study the ability of deep neural networks (DNNs) to restore missing audio content based on its context, i.e., inpaint audio gaps. We focus on a condition which has not received much attention yet: gaps in the range of tens of milliseconds. We propose a DNN structure that is provided with the signal surrounding the gap in the form of time-frequency (TF) coefficients. Two DNNs with either complex-valued TF coefficient output or magnitude TF coefficient output were studied by separately training them on inpainting two types of audio signals (music and musical instruments) having 64-ms long gaps. The magnitude DNN outperformed the complex-valued DNN in terms of signal-to-noise ratios and objective difference grades. Although, for instruments, a reference inpainting obtained through linear predictive coding performed better in both metrics, it performed worse than the magnitude DNN for music. This demonstrates the potential of the magnitude DNN, in particular for inpainting signals that are more complex than single instrument sounds.''', 
    tags = [inpaint, music_audio, lit_review_for_liwei_ijcai_2024], 
    my_notes = r'''
tens of ms gaps.  
''', 
)

inpainting_of_long_audio_segments_with_similarity_graphs = Paper(
    apa = r'''Perraudin, N., Holighaus, N., Majdak, P., & Balazs, P. (2018). Inpainting of long audio segments with similarity graphs. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 26(6), 1083-1094.''', 
    bib = r'''@article{perraudin2018inpainting,
  title={Inpainting of long audio segments with similarity graphs},
  author={Perraudin, Nathanael and Holighaus, Nicki and Majdak, Piotr and Balazs, Peter},
  journal={IEEE/ACM Transactions on Audio, Speech, and Language Processing},
  volume={26},
  number={6},
  pages={1083--1094},
  year={2018},
  publisher={IEEE}
}''', 
    abstract = r'''We present a novel method for the compensation of long duration data loss in audio signals, in particular music. The concealment of such signal defects is based on a graph that encodes signal structure in terms of time-persistent spectral similarity. A suitable candidate segment for the substitution of the lost content is proposed by an intuitive optimization scheme and smoothly inserted into the gap , i.e., the lost or distorted signal region. Extensive listening tests show that the proposed algorithm provides highly promising results when applied to a variety of real-world music signals.''', 
    tags = [inpaint, music_audio, lit_review_for_liwei_ijcai_2024, rule_based], 
    my_notes = r'''
rule-based.  
''', 
)

deepbach_a_steerable_model_for_bach_chorales_generation = Paper(
    apa = r'''Hadjeres, G., Pachet, F., & Nielsen, F. (2017, July). Deepbach: a steerable model for bach chorales generation. In International conference on machine learning (pp. 1362-1371). PMLR.''', 
    bib = r'''@inproceedings{hadjeres2017deepbach,
  title={Deepbach: a steerable model for bach chorales generation},
  author={Hadjeres, Ga{\"e}tan and Pachet, Fran{\c{c}}ois and Nielsen, Frank},
  booktitle={International conference on machine learning},
  pages={1362--1371},
  year={2017},
  organization={PMLR}
}''', 
    abstract = r'''This paper introduces DeepBach, a graphical model aimed at modeling polyphonic music and specifically hymn-like pieces. We claim that, after being trained on the chorale harmonizations by Johann Sebastian Bach, our model is capable of generating highly convincing chorales in the style of Bach. DeepBach’s strength comes from the use of pseudo-Gibbs sampling coupled with an adapted representation of musical data. This is in contrast with many automatic music composition approaches which tend to compose music sequentially. Our model is also steerable in the sense that a user can constrain the generation by imposing positional constraints such as notes, rhythms or cadences in the generated score. We also provide a plugin on top of the MuseScore music editor making the interaction with DeepBach easy to use.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024], 
    my_notes = r'''
Two RNNs to encode the context from both directions.  
pseudo-Gibbs sampling.  
''', 
)

anticipation_rnn_enforcing_unary_constraints_in_sequence_generation_with_application_to_interactive_music_generation = Paper(
    apa = r'''Hadjeres, G., & Nielsen, F. (2020). Anticipation-RNN: Enforcing unary constraints in sequence generation, with application to interactive music generation. Neural Computing and Applications, 32(4), 995-1005.''', 
    bib = r'''@article{hadjeres2020anticipation,
  title={Anticipation-RNN: Enforcing unary constraints in sequence generation, with application to interactive music generation},
  author={Hadjeres, Ga{\"e}tan and Nielsen, Frank},
  journal={Neural Computing and Applications},
  volume={32},
  number={4},
  pages={995--1005},
  year={2020},
  publisher={Springer}
}''', 
    abstract = r'''Recurrent neural networks (RNNs) are now widely used on sequence generation tasks due to their ability to learn long-range dependencies and to generate sequences of arbitrary length. However, their left-to-right generation procedure only allows a limited control from a potential user which makes them unsuitable for interactive and creative usages such as interactive music generation. This article introduces a novel architecture called anticipation-RNN which possesses the assets of the RNN-based generative models while allowing to enforce user-defined unary constraints. We demonstrate its efficiency on the task of generating melodies satisfying unary constraints in the style of the soprano parts of the J.S. Bach chorale harmonizations. Sampling using the anticipation-RNN is of the same order of complexity than sampling from the traditional RNN model. This fast and interactive generation of musical sequences opens ways to devise real-time systems that could be used for creative purposes.''', 
    tags = [inpaint, symbolic_music, lit_review_for_liwei_ijcai_2024], 
)

transformer_vae_a_hierarchical_model_for_structure_aware_and_interpretable_music_representation_learning = Paper(
    apa = r'''Jiang, J., Xia, G. G., Carlton, D. B., Anderson, C. N., & Miyakawa, R. H. (2020, May). Transformer vae: A hierarchical model for structure-aware and interpretable music representation learning. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 516-520). IEEE.''', 
    bib = r'''@inproceedings{jiang2020transformer,
  title={Transformer vae: A hierarchical model for structure-aware and interpretable music representation learning},
  author={Jiang, Junyan and Xia, Gus G and Carlton, Dave B and Anderson, Chris N and Miyakawa, Ryan H},
  booktitle={ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={516--520},
  year={2020},
  organization={IEEE}
}''', 
    abstract = r'''Structure awareness and interpretability are two of the most desired properties of music generation algorithms. Structure-aware models generate more natural and coherent music with long-term dependencies, while interpretable models are more friendly for human-computer interaction and co-creation. To achieve these two goals simultaneously, we designed the Transformer Variational AutoEncoder, a hierarchical model that unifies the efforts of two recent breakthroughs in deep music generation: 1) the Music Transformer and 2) Deep Music Analogy. The former learns long-term dependencies using attention mechanism, and the latter learns interpretable latent representations using a disentangled conditional-VAE. We showed that Transformer VAE is essentially capable of learning a context-sensitive hierarchical representation, regarding local representations as the context and the dependencies among the local representations as the global structure. By interacting with the model, we can achieve context transfer, realizing the imaginary situation of "what if" a piece is developed following the music flow of another piece.''', 
    tags = [], 
    my_notes = r'''
From the perspective of z_question:  
z is the answer.  
the question lies in h_{0...i-1}, but is not directly seen by the decoder.  
''', 
)

toolllm_facilitating_large_language_models_to_master_16000_real_world_apis = Paper(
    apa = r'''Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y., ... & Sun, M. (2023). Toolllm: Facilitating large language models to master 16000+ real-world apis. arXiv preprint arXiv:2307.16789.''', 
    bib = r'''@article{qin2023toolllm,
  title={Toolllm: Facilitating large language models to master 16000+ real-world apis},
  author={Qin, Yujia and Liang, Shihao and Ye, Yining and Zhu, Kunlun and Yan, Lan and Lu, Yaxi and Lin, Yankai and Cong, Xin and Tang, Xiangru and Qian, Bill and others},
  journal={arXiv preprint arXiv:2307.16789},
  year={2023}
}''', 
    abstract = r'''Despite the advancements of open-source large language models (LLMs), e.g., LLaMA, they remain significantly limited in tool-use capabilities, i.e., using external tools (APIs) to fulfill human instructions. The reason is that current instruction tuning largely focuses on basic language tasks but ignores the tool-use domain. This is in contrast to the excellent tool-use capabilities of state-of-the-art (SOTA) closed-source LLMs, e.g., ChatGPT. To bridge this gap, we introduce ToolLLM, a general tool-use framework encompassing data construction, model training, and evaluation. We first present ToolBench, an instruction-tuning dataset for tool use, which is constructed automatically using ChatGPT. Specifically, the construction can be divided into three stages: (i) API collection: we collect 16,464 real-world RESTful APIs spanning 49 categories from RapidAPI Hub; (ii) instruction generation: we prompt ChatGPT to generate diverse instructions involving these APIs, covering both single-tool and multi-tool scenarios; (iii) solution path annotation: we use ChatGPT to search for a valid solution path (chain of API calls) for each instruction. To enhance the reasoning capabilities of LLMs, we develop a novel depth-first search-based decision tree algorithm. It enables LLMs to evaluate multiple reasoning traces and expand the search space. Moreover, to evaluate the tool-use capabilities of LLMs, we develop an automatic evaluator: ToolEval. Based on ToolBench, we fine-tune LLaMA to obtain an LLM ToolLLaMA, and equip it with a neural API retriever to recommend appropriate APIs for each instruction. Experiments show that ToolLLaMA demonstrates a remarkable ability to execute complex instructions and generalize to unseen APIs, and exhibits comparable performance to ChatGPT. Our ToolLLaMA also demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench.''', 
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop],
    my_notes = r'''
The tool usage mindset.  
''', 
)

evaluating_explanations_how_much_do_explanations_from_the_teacher_aid_students = Paper(
    apa = r'''Pruthi, D., Bansal, R., Dhingra, B., Soares, L. B., Collins, M., Lipton, Z. C., ... & Cohen, W. W. (2022). Evaluating Explanations: How much do explanations from the teacher aid students?. Transactions of the Association for Computational Linguistics, 10, 359-375.''', 
    bib = r'''@article{pruthi2022evaluating,
  title={Evaluating Explanations: How much do explanations from the teacher aid students?},
  author={Pruthi, Danish and Bansal, Rachit and Dhingra, Bhuwan and Soares, Livio Baldini and Collins, Michael and Lipton, Zachary C and Neubig, Graham and Cohen, William W},
  journal={Transactions of the Association for Computational Linguistics},
  volume={10},
  pages={359--375},
  year={2022},
  publisher={MIT Press One Broadway, 12th Floor, Cambridge, Massachusetts 02142, USA~…}
}''', 
    abstract = r'''While many methods purport to explain predictions by highlighting salient features, what aims these explanations serve and how they ought to be evaluated often go unstated. In this work, we introduce a framework to quantify the value of explanations via the accuracy gains that they confer on a student model trained to simulate a teacher model. Crucially, the explanations are available to the student during training, but are not available at test time. Compared with prior proposals, our approach is less easily gamed, enabling principled, automatic, model-agnostic evaluation of attributions. Using our framework, we compare numerous attribution methods for text classification and question answering, and observe quantitative differences that are consistent (to a moderate to high degree) across different student model architectures and learning strategies.1''', 
    tags = [talks_at_mbzuai], 
    my_notes = r'''
Can the student model learn better with explanations from the teacher model?  
''', 
)

large_multimodal_agents_a_survey = Paper(
    apa = r'''Xie, J., Chen, Z., Zhang, R., Wan, X., & Li, G. (2024). Large Multimodal Agents: A Survey. arXiv preprint arXiv:2402.15116.''', 
    bib = r'''@article{xie2024large,
  title={Large Multimodal Agents: A Survey},
  author={Xie, Junlin and Chen, Zhihong and Zhang, Ruifei and Wan, Xiang and Li, Guanbin},
  journal={arXiv preprint arXiv:2402.15116},
  year={2024}
}''', 
    abstract = r'''Large language models (LLMs) have achieved superior performance in powering text-based AI agents, endowing them with decision-making and reasoning abilities akin to humans. Concurrently, there is an emerging research trend focused on extending these LLM-powered AI agents into the multimodal domain. This extension enables AI agents to interpret and respond to diverse multimodal user queries, thereby handling more intricate and nuanced tasks. In this paper, we conduct a systematic review of LLM-driven multimodal agents, which we refer to as large multimodal agents ( LMAs for short). First, we introduce the essential components involved in developing LMAs and categorize the current body of research into four distinct types. Subsequently, we review the collaborative frameworks integrating multiple LMAs , enhancing collective efficacy. One of the critical challenges in this field is the diverse evaluation methods used across existing studies, hindering effective comparison among different LMAs . Therefore, we compile these evaluation methodologies and establish a comprehensive framework to bridge the gaps. This framework aims to standardize evaluations, facilitating more meaningful comparisons. Concluding our review, we highlight the extensive applications of LMAs and propose possible future research directions. Our discussion aims to provide valuable insights and guidelines for future research in this rapidly evolving field. An up-to-date resource list is available at this https URL.''', 
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop], 
    my_notes = r'''
Good read. Emphasis on agent, its implementation, and the taxonomy.  
''',
)

webwise_web_interface_control_and_sequential_exploration_with_large_language_models = Paper(
    apa = r'''Tao, H., TV, S., Shlapentokh-Rothman, M., Hoiem, D., & Ji, H. (2023). Webwise: Web interface control and sequential exploration with large language models. arXiv preprint arXiv:2310.16042.''', 
    bib = r'''@article{tao2023webwise,
  title={Webwise: Web interface control and sequential exploration with large language models},
  author={Tao, Heyi and TV, Sethuraman and Shlapentokh-Rothman, Michal and Hoiem, Derek and Ji, Heng},
  journal={arXiv preprint arXiv:2310.16042},
  year={2023}
}''', 
    abstract = r'''The paper investigates using a Large Language Model (LLM) to automatically perform web software tasks using click, scroll, and text input operations. Previous approaches, such as reinforcement learning (RL) or imitation learning, are inefficient to train and task-specific. Our method uses filtered Document Object Model (DOM) elements as observations and performs tasks step-by-step, sequentially generating small programs based on the current observations. We use in-context learning, either benefiting from a single manually provided example, or an automatically generated example based on a successful zero-shot trial. We evaluate the proposed method on the MiniWob++ benchmark. With only one in-context example, our WebWISE method achieves similar or better performance than other methods that require many demonstrations or trials.''', 
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop, llm_over_GUI, llm_as_agent, multimodal_llm],
    my_notes = r'''
A nice LLM agent, but no human interaction. 
Command -> actions. No multi tools, 
but multi-round LLM-based planning.
''', 
)

empowering_llm_to_use_smartphone_for_intelligent_task_automation = Paper(
    shorts = ['AutoDroid'], 
    apa = r'''Wen, H., Li, Y., Liu, G., Zhao, S., Yu, T., Li, T. J. J., ... & Liu, Y. (2023). Empowering llm to use smartphone for intelligent task automation. arXiv preprint arXiv:2308.15272.''', 
    bib = r'''@article{wen2023empowering,
  title={Empowering llm to use smartphone for intelligent task automation},
  author={Wen, Hao and Li, Yuanchun and Liu, Guohong and Zhao, Shanhui and Yu, Tao and Li, Toby Jia-Jun and Jiang, Shiqi and Liu, Yunhao and Zhang, Yaqin and Liu, Yunxin},
  journal={arXiv preprint arXiv:2308.15272},
  year={2023}
}''', 
    abstract = r'''Mobile task automation is an attractive technique that aims to enable voice-based hands-free user interaction with smartphones. However, existing approaches suffer from poor scalability due to the limited language understanding ability and the non-trivial manual efforts required from developers or end-users. The recent advance of large language models (LLMs) in language understanding and reasoning inspires us to rethink the problem from a model-centric perspective, where task preparation, comprehension, and execution are handled by a unified language model. In this work, we introduce AutoDroid, a mobile task automation system that can handle arbitrary tasks on any Android application without manual efforts. The key insight is to combine the commonsense knowledge of LLMs and domain-specific knowledge of apps through automated dynamic analysis. The main components include a functionality-aware UI representation method that bridges the UI with the LLM, exploration-based memory injection techniques that augment the app-specific domain knowledge of LLM, and a multi-granularity query optimization module that reduces the cost of model inference. We integrate AutoDroid with off-the-shelf LLMs including online GPT-4/GPT-3.5 and on-device Vicuna, and evaluate its performance on a new benchmark for memory-augmented Android task automation with 158 common tasks. The results demonstrated that AutoDroid is able to precisely generate actions with an accuracy of 90.9%, and complete tasks with a success rate of 71.3%, outperforming the GPT-4-powered baselines by 36.4% and 39.7%. The demo, benchmark suites, and source code of AutoDroid will be released at url{this https URL}.''', 
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop, llm_over_GUI, llm_as_agent, multimodal_llm],
    my_notes = r'''
A nice LLM agent, but no human interaction. 
Command -> actions. No multi tools, 
but multi-round LLM-based planning.
'''
)

gpt_4v_in_wonderland_large_multimodal_models_for_zero_shot_smartphone_gui_navigation = Paper(
    shorts = ['MM-Navigator'],
    apa = r'''Yan, A., Yang, Z., Zhu, W., Lin, K., Li, L., Wang, J., ... & Wang, L. (2023). Gpt-4v in wonderland: Large multimodal models for zero-shot smartphone gui navigation. arXiv preprint arXiv:2311.07562.''', 
    bib = r'''@article{yan2023gpt,
  title={Gpt-4v in wonderland: Large multimodal models for zero-shot smartphone gui navigation},
  author={Yan, An and Yang, Zhengyuan and Zhu, Wanrong and Lin, Kevin and Li, Linjie and Wang, Jianfeng and Yang, Jianwei and Zhong, Yiwu and McAuley, Julian and Gao, Jianfeng and others},
  journal={arXiv preprint arXiv:2311.07562},
  year={2023}
}''', 
    abstract = r'''We present MM-Navigator, a GPT-4V-based agent for the smartphone graphical user interface (GUI) navigation task. MM-Navigator can interact with a smartphone screen as human users, and determine subsequent actions to fulfill given instructions. Our findings demonstrate that large multimodal models (LMMs), specifically GPT-4V, excel in zero-shot GUI navigation through its advanced screen interpretation, action reasoning, and precise action localization capabilities. We first benchmark MM-Navigator on our collected iOS screen dataset. According to human assessments, the system exhibited a 91\% accuracy rate in generating reasonable action descriptions and a 75\% accuracy rate in executing the correct actions for single-step instructions on iOS. Additionally, we evaluate the model on a subset of an Android screen navigation dataset, where the model outperforms previous GUI navigators in a zero-shot fashion. Our benchmark and detailed analyses aim to lay a robust groundwork for future research into the GUI navigation task. The project page is at this https URL.''', 
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop, llm_over_GUI, llm_as_agent, multimodal_llm],
    my_notes = r'''
A nice LLM agent, but no human interaction. 
Command -> actions. No multi tools, 
but multi-round LLM-based planning.  
Difference w/ empowering_llm_to_use_smartphone_for_intelligent_task_automation: 
instead of using HTML to make the UI accessible by LLM, 
they directly use GPT-4V. It's similar to 
webwise_web_interface_control_and_sequential_exploration_with_large_language_models. 
''', 
)

appagent_multimodal_agents_as_smartphone_users = Paper(
    apa = r'''Yang, Z., Liu, J., Han, Y., Chen, X., Huang, Z., Fu, B., & Yu, G. (2023). Appagent: Multimodal agents as smartphone users. arXiv preprint arXiv:2312.13771.''', 
    bib = r'''@article{yang2023appagent,
  title={Appagent: Multimodal agents as smartphone users},
  author={Yang, Zhao and Liu, Jiaxuan and Han, Yucheng and Chen, Xin and Huang, Zebiao and Fu, Bin and Yu, Gang},
  journal={arXiv preprint arXiv:2312.13771},
  year={2023}
}''',
    abstract = r'''Recent advancements in large language models (LLMs) have led to the creation of intelligent agents capable of performing complex tasks. This paper introduces a novel LLM-based multimodal agent framework designed to operate smartphone applications. Our framework enables the agent to operate smartphone applications through a simplified action space, mimicking human-like interactions such as tapping and swiping. This novel approach bypasses the need for system back-end access, thereby broadening its applicability across diverse apps. Central to our agent's functionality is its innovative learning method. The agent learns to navigate and use new apps either through autonomous exploration or by observing human demonstrations. This process generates a knowledge base that the agent refers to for executing complex tasks across different applications. To demonstrate the practicality of our agent, we conducted extensive testing over 50 tasks in 10 different applications, including social media, email, maps, shopping, and sophisticated image editing tools. The results affirm our agent's proficiency in handling a diverse array of high-level tasks.''', 
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop, llm_over_GUI, llm_as_agent, multimodal_llm],
    my_notes = r'''
A nice LLM agent, but no human interaction. 
Command -> actions. No multi tools, 
but multi-round LLM-based planning.  
''', 
)

you_only_look_at_screens_multimodal_chain_of_action_agents = Paper(
    shorts = ['Auto-UI'],
    apa = r'''Zhan, Z., & Zhang, A. (2023). You only look at screens: Multimodal chain-of-action agents. arXiv preprint arXiv:2309.11436.''',
    bib = r'''@article{zhan2023you,
  title={You only look at screens: Multimodal chain-of-action agents},
  author={Zhan, Zhuosheng and Zhang, Aston},
  journal={arXiv preprint arXiv:2309.11436},
  year={2023}
}''',
    abstract = r'''Autonomous user interface (UI) agents aim to facilitate task automation by interacting with the user interface without manual intervention. Recent studies have investigated eliciting the capabilities of large language models (LLMs) for effective engagement in diverse environments. To align with the input-output requirement of LLMs, existing approaches are developed under a sandbox setting where they rely on external tools and application-specific APIs to parse the environment into textual elements and interpret the predicted actions. Consequently, those approaches often grapple with inference inefficiency and error propagation risks. To mitigate the challenges, we introduce Auto-UI, a multimodal solution that directly interacts with the interface, bypassing the need for environment parsing or reliance on application-dependent APIs. Moreover, we propose a chain-of-action technique -- leveraging a series of intermediate previous action histories and future action plans -- to help the agent decide what action to execute. We evaluate our approach on a new device-control benchmark AITW with 30K unique instructions, spanning multi-step tasks such as application operation, web searching, and web shopping. Experimental results show that Auto-UI achieves state-of-the-art performance with an action type prediction accuracy of 90% and an overall action success rate of 74%. Code is publicly available at this https URL.''',
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop, llm_over_GUI, llm_as_agent, multimodal_llm],
    my_notes = r'''
A nice LLM agent, but no human interaction. 
Command -> actions. No multi tools, 
but multi-round LLM-based planning.  
''', 
)

droidbot_gpt_gpt_powered_ui_automation_for_android = Paper(
    shorts = ['DroidBot-GPT'],
    apa = r'''Wen, H., Wang, H., Liu, J., & Li, Y. (2023). DroidBot-GPT: GPT-powered UI Automation for Android. arXiv preprint arXiv:2304.07061.''', 
    bib = r'''@article{wen2023droidbot,
  title={DroidBot-GPT: GPT-powered UI Automation for Android},
  author={Wen, Hao and Wang, Hongming and Liu, Jiaxuan and Li, Yuanchun},
  journal={arXiv preprint arXiv:2304.07061},
  year={2023}
}''',
    abstract = r'''This paper introduces DroidBot-GPT, a tool that utilizes GPT-like large language models (LLMs) to automate the interactions with Android mobile applications. Given a natural language description of a desired task, DroidBot-GPT can automatically generate and execute actions that navigate the app to complete the task. It works by translating the app GUI state information and the available actions on the smartphone screen to natural language prompts and asking the LLM to make a choice of actions. Since the LLM is typically trained on a large amount of data including the how-to manuals of diverse software applications, it has the ability to make reasonable choices of actions based on the provided information. We evaluate DroidBot-GPT with a self-created dataset that contains 33 tasks collected from 17 Android applications spanning 10 categories. It can successfully complete 39.39% of the tasks, and the average partial completion progress is about 66.76%. Given the fact that our method is fully unsupervised (no modification required from both the app and the LLM), we believe there is great potential to enhance automation performance with better app development paradigms and/or custom model training.''', 
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop, llm_over_GUI, llm_as_agent, multimodal_llm],
    my_notes = r'''
A nice LLM agent, but no human interaction
Command -> actions. No multi tools,
but multi-round LLM-based planning.
''', 
)

explore_select_derive_and_recall_augmenting_llm_with_human_like_memory_for_mobile_task_automation = Paper(
    shorts = ['MemoDroid'],
    apa = r'''Lee, S., Choi, J., Lee, J., Choi, H., Ko, S. Y., Oh, S., & Shin, I. (2023). Explore, select, derive, and recall: Augmenting llm with human-like memory for mobile task automation. arXiv preprint arXiv:2312.03003.''',
    bib = r'''@article{lee2023explore,
  title={Explore, select, derive, and recall: Augmenting llm with human-like memory for mobile task automation},
  author={Lee, Sunjae and Choi, Junyoung and Lee, Jungjae and Choi, Hojun and Ko, Steven Y and Oh, Sangeun and Shin, Insik},
  journal={arXiv preprint arXiv:2312.03003},
  year={2023}
}''',
    abstract = r'''The advent of large language models (LLMs) has opened up new opportunities in the field of mobile task automation. Their superior language understanding and reasoning capabilities allow users to automate complex and repetitive tasks. However, due to the inherent unreliability and high operational cost of LLMs, their practical applicability is quite limited. To address these issues, this paper introduces MemoDroid, an innovative LLM-based mobile task automator enhanced with a unique app memory. MemoDroid emulates the cognitive process of humans interacting with a mobile app -- explore, select, derive, and recall. This approach allows for a more precise and efficient learning of a task's procedure by breaking it down into smaller, modular components that can be re-used, re-arranged, and adapted for various objectives. We implement MemoDroid using online LLMs services (GPT-3.5 and GPT-4) and evaluate its performance on 50 unique mobile tasks across 5 widely used mobile apps. The results indicate that MemoDroid can adapt learned tasks to varying contexts with 100% accuracy and reduces their latency and cost by 69.22% and 77.36% compared to a GPT-4 powered baseline.''',
    tags = [lit_review_for_hci_ijcai_2024, llm_in_the_loop, llm_over_GUI, llm_as_agent, multimodal_llm],
    my_notes = r'''
A nice LLM agent, but no human interaction
Command -> actions. No multi tools,
but multi-round LLM-based planning.
Compared to others, this one is more deploy-ready with engineering and less novel.  
''', 
)

assistgui_task_oriented_desktop_graphical_user_interface_automation = Paper(
    shorts = ['AssistGUI'],
    apa = r'''Gao, D., Ji, L., Bai, Z., Ouyang, M., Li, P., Mao, D., ... & Shou, M. Z. (2023). Assistgui: Task-oriented desktop graphical user interface automation. arXiv preprint arXiv:2312.13108.''',
    bib = r'''@article{gao2023assistgui,
  title={Assistgui: Task-oriented desktop graphical user interface automation},
  author={Gao, Difei and Ji, Lei and Bai, Zechen and Ouyang, Mingyu and Li, Peiran and Mao, Dongxing and Wu, Qinchen and Zhang, Weichen and Wang, Peiyi and Guo, Xiangwu and others},
  journal={arXiv preprint arXiv:2312.13108},
  year={2023}
}''',
    abstract = r'''Graphical User Interface (GUI) automation holds significant promise for assisting users with complex tasks, thereby boosting human productivity. Existing works leveraging Large Language Model (LLM) or LLM-based AI agents have shown capabilities in automating tasks on Android and Web platforms. However, these tasks are primarily aimed at simple device usage and entertainment operations. This paper presents a novel benchmark, AssistGUI, to evaluate whether models are capable of manipulating the mouse and keyboard on the Windows platform in response to user-requested tasks. We carefully collected a set of 100 tasks from nine widely-used software applications, such as, After Effects and MS Word, each accompanied by the necessary project files for better evaluation. Moreover, we propose an advanced Actor-Critic Embodied Agent framework, which incorporates a sophisticated GUI parser driven by an LLM-agent and an enhanced reasoning mechanism adept at handling lengthy procedural tasks. Our experimental results reveal that our GUI Parser and Reasoning mechanism outshine existing methods in performance. Nevertheless, the potential remains substantial, with the best model attaining only a 46% success rate on our benchmark. We conclude with a thorough analysis of the current methods' limitations, setting the stage for future breakthroughs in this domain.''',
    tags = [lit_review_for_hci_ijcai_2024, llm_over_GUI],
    my_notes = r'''
It's a benchmark.
''', 
)

modelscope_agent_building_your_customizable_agent_system_with_open_source_large_language_models = Paper(
    shorts = ['ModelScope-Agent'],
    apa = r'''Li, C., Chen, H., Yan, M., Shen, W., Xu, H., Wu, Z., ... & Zhou, J. (2023). Modelscope-agent: Building your customizable agent system with open-source large language models. arXiv preprint arXiv:2309.00986.''',
    bib = r'''@article{li2023modelscope,
  title={Modelscope-agent: Building your customizable agent system with open-source large language models},
  author={Li, Chenliang and Chen, Hehong and Yan, Ming and Shen, Weizhou and Xu, Haiyang and Wu, Zhikai and Zhang, Zhicheng and Zhou, Wenmeng and Chen, Yingda and Cheng, Chen and others},
  journal={arXiv preprint arXiv:2309.00986},
  year={2023}
}''',
    abstract = r'''Large language models (LLMs) have recently demonstrated remarkable capabilities to comprehend human intentions, engage in reasoning, and design planning-like behavior. To further unleash the power of LLMs to accomplish complex tasks, there is a growing trend to build agent framework that equips LLMs, such as ChatGPT, with tool-use abilities to connect with massive external APIs. In this work, we introduce ModelScope-Agent, a general and customizable agent framework for real-world applications, based on open-source LLMs as controllers. It provides a user-friendly system library, with customizable engine design to support model training on multiple open-source LLMs, while also enabling seamless integration with both model APIs and common APIs in a unified way. To equip the LLMs with tool-use abilities, a comprehensive framework has been proposed spanning over tool-use data collection, tool retrieval, tool registration, memory control, customized model training, and evaluation for practical real-world applications. Finally, we showcase ModelScopeGPT, a real-world intelligent assistant of ModelScope Community based on the ModelScope-Agent framework, which is able to connect open-source LLMs with more than 1000 public AI models and localized community knowledge in ModelScope. The ModelScope-Agent library\footnote{this https URL} and online demo\footnote{this https URL} are now publicly available.''',
    tags = [lit_review_for_hci_ijcai_2024],
    my_notes = r'''
It's a framework. 
''', 
)

assistgpt_a_general_multi_modal_assistant_that_can_plan_execute_inspect_and_learn = Paper(
    apa = r'''Gao, D., Ji, L., Zhou, L., Lin, K. Q., Chen, J., Fan, Z., & Shou, M. Z. (2023). AssistGPT: A General Multi-modal Assistant that can Plan, Execute, Inspect, and Learn. arXiv preprint arXiv:2306.08640.''', 
    bib = r'''@article{gao2023assistgpt,
  title={AssistGPT: A General Multi-modal Assistant that can Plan, Execute, Inspect, and Learn},
  author={Gao, Difei and Ji, Lei and Zhou, Luowei and Lin, Kevin Qinghong and Chen, Joya and Fan, Zihan and Shou, Mike Zheng},
  journal={arXiv preprint arXiv:2306.08640},
  year={2023}
}''',
    abstract = r'''Recent research on Large Language Models (LLMs) has led to remarkable advancements in general NLP AI assistants. Some studies have further explored the use of LLMs for planning and invoking models or APIs to address more general multi-modal user queries. Despite this progress, complex visual-based tasks still remain challenging due to the diverse nature of visual tasks. This diversity is reflected in two aspects: 1) Reasoning paths. For many real-life applications, it is hard to accurately decompose a query simply by examining the query itself. Planning based on the specific visual content and the results of each step is usually required. 2) Flexible inputs and intermediate results. Input forms could be flexible for in-the-wild cases, and involves not only a single image or video but a mixture of videos and images, e.g., a user-view image with some reference videos. Besides, a complex reasoning process will also generate diverse multimodal intermediate results, e.g., video narrations, segmented video clips, etc. To address such general cases, we propose a multi-modal AI assistant, AssistGPT, with an interleaved code and language reasoning approach called Plan, Execute, Inspect, and Learn (PEIL) to integrate LLMs with various tools. Specifically, the Planner is capable of using natural language to plan which tool in Executor should do next based on the current reasoning progress. Inspector is an efficient memory manager to assist the Planner to feed proper visual information into a specific tool. Finally, since the entire reasoning process is complex and flexible, a Learner is designed to enable the model to autonomously explore and discover the optimal solution. We conducted experiments on A-OKVQA and NExT-QA benchmarks, achieving state-of-the-art results. Moreover, showcases demonstrate the ability of our system to handle questions far more complex than those found in the benchmarks.''',
    tags = [lit_review_for_hci_ijcai_2024],
)

a_framework_for_creating_natural_language_user_interfaces_for_action_based_applications = Paper(
    apa = r'''Chong, S., & Pucella, R. (2004). A framework for creating natural language user interfaces for action-based applications. arXiv preprint cs/0412065.''',
    bib = r'''@article{chong2004framework,
  title={A framework for creating natural language user interfaces for action-based applications},
  author={Chong, Stephen and Pucella, Riccardo},
  journal={arXiv preprint cs/0412065},
  year={2004}
}''',
    abstract = r'''In this paper we present a framework for creating natural language interfaces to action-based applications. Our framework uses a number of reusable application-independent components, in order to reduce the effort of creating a natural language interface for a given application. Using a type-logical grammar, we first translate natural language sentences into expressions in an extended higher-order logic. These expressions can be seen as executable specifications corresponding to the original sentences. The executable specifications are then interpreted by invoking appropriate procedures provided by the application for which a natural language interface is being created.''',
    tags = [lit_review_for_hci_ijcai_2024],
    my_notes = r'''
Rule-based parsing of NL.
''', 
)

natural_language_user_interface_for_software_engineering_tasks = Paper(
    apa = r'''Wachtel, A., Klamroth, J., & Tichy, W. F. (2017, March). Natural language user interface for software engineering tasks. In Proceedings of the International Conference on Advances in Computer-Human Interactions (ACHI) (Vol. 10, pp. 34-39).''',
    bib = r'''@inproceedings{wachtel2017natural,
  title={Natural language user interface for software engineering tasks},
  author={Wachtel, Alexander and Klamroth, Jonas and Tichy, Walter F},
  booktitle={Proceedings of the International Conference on Advances in Computer-Human Interactions (ACHI)},
  volume={10},
  pages={34--39},
  year={2017}
}''', 
    abstract = r'''In this paper, we present the idea to use natural language as the user interface for programming tasks. Programming languages assist with repetitive tasks that involve the use of conditionals, loops and statements. This is what is often challenging users. However, users can easily describe tasks in their natural language. We aim to develop a Natural Language User Interface that enables users to describe algorithms, including statements, loops, and conditionals. For this, we extend our current spreadsheet system to support control flows. An evaluation shows that users solved more than 60% of tasks. Although far from perfect, this research might lead to fundamental changes in computer use. With natural language, programming would become available to everyone. We believe that it is a reasonable approach for end user software engineering and will therefore overcome the present bottleneck of IT proficients.''',
    tags = [lit_review_for_hci_ijcai_2024],
)

tell_me_more_towards_implicit_user_intention_understanding_of_language_model_driven_agents = Paper(
    apa = r'''Qian, C., He, B., Zhuang, Z., Deng, J., Qin, Y., Cong, X., ... & Sun, M. (2024). Tell Me More! Towards Implicit User Intention Understanding of Language Model Driven Agents. arXiv preprint arXiv:2402.09205.''',
    bib = r'''@article{qian2024tell,
  title={Tell Me More! Towards Implicit User Intention Understanding of Language Model Driven Agents},
  author={Qian, Cheng and He, Bingxiang and Zhuang, Zhong and Deng, Jia and Qin, Yujia and Cong, Xin and Lin, Yankai and Zhang, Zhong and Liu, Zhiyuan and Sun, Maosong},
  journal={arXiv preprint arXiv:2402.09205},
  year={2024}
}''',
    abstract = r'''Current language model-driven agents often lack mechanisms for effective user participation, which is crucial given the vagueness commonly found in user instructions. Although adept at devising strategies and performing tasks, these agents struggle with seeking clarification and grasping precise user intentions. To bridge this gap, we introduce Intention-in-Interaction (IN3), a novel benchmark designed to inspect users' implicit intentions through explicit queries. Next, we propose the incorporation of model experts as the upstream in agent designs to enhance user-agent interaction. Employing IN3, we empirically train Mistral-Interact, a powerful model that proactively assesses task vagueness, inquires user intentions, and refines them into actionable goals before starting downstream agent task execution. Integrating it into the XAgent framework, we comprehensively evaluate the enhanced agent system regarding user instruction understanding and execution, revealing that our approach notably excels at identifying vague user tasks, recovering and summarizing critical missing information, setting precise and necessary agent execution goals, and minimizing redundant tool usage, thus boosting overall efficiency. All the data and codes are released.''',
    tags = [lit_review_for_hci_ijcai_2024, hci, llm_as_agent],
)

simple_and_controllable_music_generation = Paper(
    shorts = ['MusicGen'],
    apa = r'''Copet, J., Kreuk, F., Gat, I., Remez, T., Kant, D., Synnaeve, G., ... & Défossez, A. (2024). Simple and controllable music generation. Advances in Neural Information Processing Systems, 36.''',
    bib = r'''@article{copet2024simple,
  title={Simple and controllable music generation},
  author={Copet, Jade and Kreuk, Felix and Gat, Itai and Remez, Tal and Kant, David and Synnaeve, Gabriel and Adi, Yossi and D{\'e}fossez, Alexandre},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
}''',
    abstract = r'''We tackle the task of conditional music generation. We introduce MusicGen, a single Language Model (LM) that operates over several streams of compressed discrete music representation, i.e., tokens. Unlike prior work, MusicGen is comprised of a single-stage transformer LM together with efficient token interleaving patterns, which eliminates the need for cascading several models, e.g., hierarchically or upsampling. Following this approach, we demonstrate how MusicGen can generate high-quality samples, both mono and stereo, while being conditioned on textual description or melodic features, allowing better controls over the generated output. We conduct extensive empirical evaluation, considering both automatic and human studies, showing the proposed approach is superior to the evaluated baselines on a standard text-to-music benchmark. Through ablation studies, we shed light over the importance of each of the components comprising MusicGen. Music samples, code, and models are available at https://github.com/facebookresearch/audiocraft''',
    tags = [llm, generation, transformer, control],
)

minigpt_5_interleaved_vision_and_language_generation_via_generative_vokens = Paper(
    shorts = ['MiniGPT-5'],
    apa = r'''Zheng, K., He, X., & Wang, X. E. (2023). Minigpt-5: Interleaved vision-and-language generation via generative vokens. arXiv preprint arXiv:2310.02239.''',
    bib = r'''@article{zheng2023minigpt,
  title={Minigpt-5: Interleaved vision-and-language generation via generative vokens},
  author={Zheng, Kaizhi and He, Xuehai and Wang, Xin Eric},
  journal={arXiv preprint arXiv:2310.02239},
  year={2023}
}''',
    abstract = r'''The effectiveness of Multimodal Large Language Models (MLLMs) demonstrates a profound capability in multimodal understanding. However, the simultaneous generation of images with coherent texts is still underdeveloped. Addressing this, we introduce a novel interleaved vision-and-language generation method, centered around the concept of ``generative vokens". These vokens serve as pivotal elements contributing to coherent image-text outputs. Our method is marked by a unique two-stage training strategy for description-free multimodal generation, which does not necessitate extensive descriptions of images. We integrate classifier-free guidance to enhance the alignment of generated images and texts, ensuring more seamless and contextually relevant multimodal interactions. Our model, MiniGPT-5, exhibits substantial improvement over the baseline models on multimodal generation datasets, including MMDialog and VIST. The human evaluation shows MiniGPT-5 is better than the baseline model on more than 56\% cases for multimodal generation, highlighting its efficacy across diverse benchmarks.''',
    tags = [llm, multimodal_llm],
)

next_gpt_any_to_any_multimodal_llm = Paper(
    shorts = ['NExT-GPT'],
    apa = r'''Wu, S., Fei, H., Qu, L., Ji, W., & Chua, T. S. (2023). Next-gpt: Any-to-any multimodal llm. arXiv preprint arXiv:2309.05519.''', 
    bib = r'''@article{wu2023next,
  title={Next-gpt: Any-to-any multimodal llm},
  author={Wu, Shengqiong and Fei, Hao and Qu, Leigang and Ji, Wei and Chua, Tat-Seng},
  journal={arXiv preprint arXiv:2309.05519},
  year={2023}
}''', 
    abstract = r'''While recently Multimodal Large Language Models (MM-LLMs) have made exciting strides, they mostly fall prey to the limitation of only input-side multimodal understanding, without the ability to produce content in multiple modalities. As we humans always perceive the world and communicate with people through various modalities, developing any-to-any MM-LLMs capable of accepting and delivering content in any modality becomes essential to human-level AI. To fill the gap, we present an end-to-end general-purpose any-to-any MM-LLM system, NExT-GPT. We connect an LLM with multimodal adaptors and different diffusion decoders, enabling NExT-GPT to perceive inputs and generate outputs in arbitrary combinations of text, images, videos, and audio. By leveraging the existing well-trained highly-performing encoders and decoders, NExT-GPT is tuned with only a small amount of parameter (1%) of certain projection layers, which not only benefits low-cost training and also facilitates convenient expansion to more potential modalities. Moreover, we introduce a modality-switching instruction tuning (MosIT) and manually curate a high-quality dataset for MosIT, based on which NExT-GPT is empowered with complex cross-modal semantic understanding and content generation. Overall, our research showcases the promising possibility of building an AI agent capable of modeling universal modalities, paving the way for more human-like AI research in the community. Project page: this https URL''', 
    tags = [llm, multimodal_llm],
)

generating_images_with_multimodal_language_models = Paper(
    shorts = ['GILL'], 
    apa = r'''Koh, J. Y., Fried, D., & Salakhutdinov, R. R. (2024). Generating images with multimodal language models. Advances in Neural Information Processing Systems, 36.''',
    bib = r'''@article{koh2024generating,
  title={Generating images with multimodal language models},
  author={Koh, Jing Yu and Fried, Daniel and Salakhutdinov, Russ R},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
}''', 
    abstract = r'''We propose a method to fuse frozen text-only large language models (LLMs) with pre-trained image encoder and decoder models, by mapping between their embedding spaces. Our model demonstrates a wide suite of multimodal capabilities: image retrieval, novel image generation, and multimodal dialogue. Ours is the first approach capable of conditioning on arbitrarily interleaved image and text inputs to generate coherent image (and text) outputs. To achieve strong performance on image generation, we propose an efficient mapping network to ground the LLM to an off-the-shelf text-to-image generation model. This mapping network translates hidden representations of text into the embedding space of the visual models, enabling us to leverage the strong text representations of the LLM for visual outputs. Our approach outperforms baseline generation models on tasks with longer and more complex language. In addition to novel image generation, our model is also capable of image retrieval from a prespecified dataset, and decides whether to retrieve or generate at inference time. This is done with a learnt decision module which conditions on the hidden representations of the LLM. Our model exhibits a wider range of capabilities compared to prior multimodal language models. It can process image-and-text inputs, and produce retrieved images, generated images, and generated text — outperforming non-LLM based generation models across several text-to-image tasks that measure context dependence.''',
    tags = [llm, multimodal_llm],
)

audioldm_2_learning_holistic_audio_generation_with_self_supervised_pretraining = Paper(
    shorts = ['AudioLDM 2'],
    apa = r'''Liu, H., Tian, Q., Yuan, Y., Liu, X., Mei, X., Kong, Q., ... & Plumbley, M. D. (2023). AudioLDM 2: Learning holistic audio generation with self-supervised pretraining. arXiv preprint arXiv:2308.05734.''', 
    bib = r'''@article{liu2023audioldm2,
  title={{AudioLDM 2}: Learning Holistic Audio Generation with Self-supervised Pretraining},
  author={Haohe Liu and Qiao Tian and Yi Yuan and Xubo Liu and Xinhao Mei and Qiuqiang Kong and Yuping Wang and Wenwu Wang and Yuxuan Wang and Mark D. Plumbley},
  journal={arXiv preprint arXiv:2308.05734},
  year={2023}
}''', 
    abstract = r'''Although audio generation shares commonalities across different types of audio, such as speech, music, and sound effects, designing models for each type requires careful consideration of specific objectives and biases that can significantly differ from those of other types. To bring us closer to a unified perspective of audio generation, this paper proposes a framework that utilizes the same learning method for speech, music, and sound effect generation. Our framework introduces a general representation of audio, called "language of audio" (LOA). Any audio can be translated into LOA based on AudioMAE, a self-supervised pre-trained representation learning model. In the generation process, we translate any modalities into LOA by using a GPT-2 model, and we perform self-supervised audio generation learning with a latent diffusion model conditioned on LOA. The proposed framework naturally brings advantages such as in-context learning abilities and reusable self-supervised pretrained AudioMAE and latent diffusion models. Experiments on the major benchmarks of text-to-audio, text-to-music, and text-to-speech demonstrate state-of-the-art or competitive performance against previous approaches. Our code, pretrained model, and demo are available at this https URL.''',
    tags = [llm, multimodal_llm],
)

improving_convergence_and_generalization_using_parameter_symmetries = Paper(
    apa = r'''Zhao, B., Gower, R. M., Walters, R., & Yu, R. (2023). Improving Convergence and Generalization Using Parameter Symmetries. arXiv preprint arXiv:2305.13404.''', 
    bib = r'''@article{zhao2023improving,
  title={Improving Convergence and Generalization Using Parameter Symmetries},
  author={Zhao, Bo and Gower, Robert M and Walters, Robin and Yu, Rose},
  journal={arXiv preprint arXiv:2305.13404},
  year={2023}
}''', 
    abstract = r'''In many neural networks, different values of the parameters may result in the same loss value. Parameter space symmetries are loss-invariant transformations that change the model parameters. Teleportation applies such transformations to accelerate optimization. However, the exact mechanism behind this algorithm's success is not well understood. In this paper, we show that teleportation not only speeds up optimization in the short-term, but gives overall faster time to convergence. Additionally, teleporting to minima with different curvatures improves generalization, which suggests a connection between the curvature of the minimum and generalization ability. Finally, we show that integrating teleportation into a wide range of optimization algorithms and optimization-based meta-learning improves convergence. Our results showcase the versatility of teleportation and demonstrate the potential of incorporating symmetry in optimization.''', 
    tags = [symmetry], 
)

neural_teleportation = Paper(
    apa = r'''Armenta, M., Judge, T., Painchaud, N., Skandarani, Y., Lemaire, C., Gibeau Sanchez, G., ... & Jodoin, P. M. (2023). Neural teleportation. Mathematics, 11(2), 480.''', 
    bib = r'''@article{armenta2023neural,
  title={Neural teleportation},
  author={Armenta, Marco and Judge, Thierry and Painchaud, Nathan and Skandarani, Youssef and Lemaire, Carl and Gibeau Sanchez, Gabriel and Spino, Philippe and Jodoin, Pierre-Marc},
  journal={Mathematics},
  volume={11},
  number={2},
  pages={480},
  year={2023},
  publisher={MDPI}
}''', 
    abstract = r'''In this paper, we explore a process called neural teleportation, a mathematical consequence of applying quiver representation theory to neural networks. Neural teleportation teleports a network to a new position in the weight space and preserves its function. This phenomenon comes directly from the definitions of representation theory applied to neural networks and it turns out to be a very simple operation that has remarkable properties. We shed light on the surprising and counter-intuitive consequences neural teleportation has on the loss landscape. In particular, we show that teleportation can be used to explore loss level curves, that it changes the local loss landscape, sharpens global minima and boosts back-propagated gradients at any moment during the learning process.''', 
    tags = [optimization], 
)

the_representation_theory_of_neural_networks = Paper(
    apa = r'''Armenta, M., & Jodoin, P. M. (2021). The representation theory of neural networks. Mathematics, 9(24), 3216.''',
    bib = r'''@article{armenta2021representation,
  title={The representation theory of neural networks},
  author={Armenta, Marco and Jodoin, Pierre-Marc},
  journal={Mathematics},
  volume={9},
  number={24},
  pages={3216},
  year={2021},
  publisher={MDPI}
}''', 
    abstract = r'''In this work, we show that neural networks can be represented via the mathematical theory of quiver representations. More specifically, we prove that a neural network is a quiver representation with activation functions, a mathematical object that we represent using a network quiver. Furthermore, we show that network quivers gently adapt to common neural network concepts such as fully connected layers, convolution operations, residual connections, batch normalization, pooling operations and even randomly wired neural networks. We show that this mathematical representation is by no means an approximation of what neural networks are as it exactly matches reality. This interpretation is algebraic and can be studied with algebraic methods. We also provide a quiver representation model to understand how a neural network creates representations from the data. We show that a neural network saves the data as quiver representations, and maps it to a geometrical space called the moduli space, which is given in terms of the underlying oriented graph of the network, i.e., its quiver. This results as a consequence of our defined objects and of understanding how the neural network computes a prediction in a combinatorial and algebraic way. Overall, representing neural networks through the quiver representation theory leads to 9 consequences and 4 inquiries for future research that we believe are of great interest to better understand what neural networks are and how they work.''', 
)

emergent_communication_with_conversational_repair = Paper(
    apa = r'''Nikolaus, M. (2023, October). Emergent Communication with Conversational Repair. In The Twelfth International Conference on Learning Representations.''',
    bib = r'''@inproceedings{nikolaus2023emergent,
  title={Emergent Communication with Conversational Repair},
  author={Nikolaus, Mitja},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2023}
}''', 
    abstract = r'''Research on conversation has put emphasis on the importance of a multi-level communication system, in which the interlocutors aim to establish and maintain common ground. In natural conversations, repair mechanisms such as clarification requests are frequently used to improve mutual understanding. Here we explore the effects of conversational repair on languages emerging in signaling games. We extend the basic Lewis signaling game setup with a feedback channel that allows for the transmission of messages backwards from the receiver to the sender. Further, we add noise to the communication channel so that repair mechanisms become necessary for optimal performance. We find that languages emerging in setups with feedback channel are less compositional. However, the models still achieve a substantially higher generalization performance in conditions with noise, putting to question the role of compositionality for generalization. These findings generalize also to a more realistic case involving a guessing game with naturalistic images. More broadly speaking, this study provides an important step towards the creation of signaling games that more closely resemble the conditions under which human languages emerged.''', 
)

signatures_of_cross_modal_alignment_in_children_s_early_concepts = Paper(
    apa = r'''Aho, K., Roads, B. D., & Love, B. C. (2023). Signatures of cross-modal alignment in children’s early concepts. Proceedings of the National Academy of Sciences, 120(42), e2309688120.''',
    bib = r'''@article{aho2023signatures,
  title={Signatures of cross-modal alignment in children’s early concepts},
  author={Aho, Kaarina and Roads, Brett D and Love, Bradley C},
  journal={Proceedings of the National Academy of Sciences},
  volume={120},
  number={42},
  pages={e2309688120},
  year={2023},
  publisher={National Acad Sciences}
}''',
    abstract = r'''Whether supervised or unsupervised, human and machine learning is usually characterized as event-based. However, learning may also proceed by systems alignment in which mappings are inferred between entire systems, such as visual and linguistic systems. Systems alignment is possible because items that share similar visual contexts, such as a car and a truck, will also tend to share similar linguistic contexts. Because of the mirrored similarity relationships across systems, the visual and linguistic systems can be aligned at some later time absent either input. In a series of simulation studies, we considered whether children’s early concepts support systems alignment. We found that children’s early concepts are close to optimal for inferring novel concepts through systems alignment, enabling agents to correctly infer more than 85% of visual–word mappings absent supervision. One possible explanation for why children’s early concepts support systems alignment is that they are distinguished structurally by their dense semantic neighborhoods. Artificial agents using these structural features to select concepts proved highly effective, both in environments mirroring children’s conceptual world and those that exclude the concepts that children commonly acquire. For children, systems alignment and event-based learning likely complement one another. Likewise, artificial systems can benefit from incorporating these developmental principles.''',
    tags = [cross_modal_align], 
)

categorical_reparameterization_with_gumbel_softmax = Paper(
    apa = r'''Jang, E., Gu, S., & Poole, B. (2016). Categorical reparameterization with gumbel-softmax. arXiv preprint arXiv:1611.01144.''',
    bib = r'''@article{jang2016categorical,
  title={Categorical reparameterization with gumbel-softmax},
  author={Jang, Eric and Gu, Shixiang and Poole, Ben},
  journal={arXiv preprint arXiv:1611.01144},
  year={2016}
}''',
    abstract = r'''     Categorical variables are a natural choice for representing discrete structure in the world. However, stochastic neural networks rarely use categorical latent variables due to the inability to backpropagate through samples. In this work, we present an efficient gradient estimator that replaces the non-differentiable sample from a categorical distribution with a differentiable sample from a novel Gumbel-Softmax distribution. This distribution has the essential property that it can be smoothly annealed into a categorical distribution. We show that our Gumbel-Softmax estimator outperforms state-of-the-art gradient estimators on structured output prediction and unsupervised generative modeling tasks with categorical latent variables, and enables large speedups on semi-supervised classification. ''',
)
