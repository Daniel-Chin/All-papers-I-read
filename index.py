from tags import *

class theme_transformer:
    apa = 'Shih, Y. J., Wu, S. L., Zalkow, F., Müller, M., & Yang, Y. H. (2021). Theme Transformer: Symbolic Music Generation with Theme-Conditioned Transformer. arXiv preprint arXiv:2111.04093.'
    bib = '''@article{shih2021theme,
  title={Theme Transformer: Symbolic Music Generation with Theme-Conditioned Transformer},
  author={Shih, Yi-Jen and Wu, Shih-Lun and Zalkow, Frank and M{\"u}ller, Meinard and Yang, Yi-Hsuan},
  journal={arXiv preprint arXiv:2111.04093},
  year={2021}
}'''
    abstract = '''Attention-based Transformer models have been increasingly employed for automatic music generation. To condition the generation process of such a model with a user-specified sequence, a popular approach is to take that conditioning sequence as a priming sequence and ask a Transformer decoder to generate a continuation. However, this prompt-based conditioning cannot guarantee that the conditioning sequence would develop or even simply repeat itself in the generated continuation. In this paper, we propose an alternative conditioning approach, called theme-based conditioning, that explicitly trains the Transformer to treat the conditioning sequence as a thematic material that has to manifest itself multiple times in its generation result. This is achieved with two main technical contributions. First, we propose a deep learning-based approach that uses contrastive representation learning and clustering to automatically retrieve thematic materials from music pieces in the training data. Second, we propose a novel gated parallel attention module to be used in a sequence-to-sequence (seq2seq) encoder/decoder architecture to more effectively account for a given conditioning thematic material in the generation process of the Transformer decoder. We report on objective and subjective evaluations of variants of the proposed Theme Transformer and the conventional prompt-based baseline, showing that our best model can generate, to some extent, polyphonic pop piano music with repetition and plausible variations of a given condition.
'''
    tags = [transformer, music_knowledge, contrastive]
    my_notes = None

class Melon_form_then_content:
    apa = 'Zou, Y., Zou, P., Zhao, Y., Zhang, K., Zhang, R., & Wang, X. (2021). MELONS: generating melody with long-term structure using transformers and structure graph. arXiv preprint arXiv:2110.05020.'
    bib = '''@article{zou2021melons,
  title={MELONS: generating melody with long-term structure using transformers and structure graph},
  author={Zou, Yi and Zou, Pei and Zhao, Yi and Zhang, Kaixiang and Zhang, Ran and Wang, Xiaorui},
  journal={arXiv preprint arXiv:2110.05020},
  year={2021}
}'''
    abstract = '''The creation of long melody sequences requires effective expression of coherent musical structure. However, there is no clear representation of musical structure. Recent works on music generation have suggested various approaches to deal with the structural information of music, but generating a full-song melody with clear long-term structure remains a challenge. In this paper, we propose MELONS, a melody generation framework based on a graph representation of music structure which consists of eight types of bar-level relations. MELONS adopts a multi-step generation method with transformer-based networks by factoring melody generation into two sub-problems: structure generation and structure conditional melody generation. Experimental results show that MELONS can produce structured melodies with high quality and rich contents.
'''
    tags = [hierarchical, generation, structure, relation, music_knowledge, transformer]
    my_notes = '''
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
'''

class KLI:
    apa = 'Koedinger, K. R., Corbett, A. T., & Perfetti, C. (2012). The Knowledge‐Learning‐Instruction framework: Bridging the science‐practice chasm to enhance robust student learning. Cognitive science, 36(5), 757-798.'
    bib = '''@article{koedinger2012knowledge,
  title={The Knowledge-Learning-Instruction framework: Bridging the science-practice chasm to enhance robust student learning},
  author={Koedinger, Kenneth R and Corbett, Albert T and Perfetti, Charles},
  journal={Cognitive science},
  volume={36},
  number={5},
  pages={757--798},
  year={2012},
  publisher={Wiley Online Library}
}'''
    tags = [psychology, education]
    my_notes = '''
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
'''

class Jukebox:
    apa = 'Dhariwal, P., Jun, H., Payne, C., Kim, J. W., Radford, A., & Sutskever, I. (2020). Jukebox: A generative model for music. arXiv preprint arXiv:2005.00341.'
    bib = '''@article{dhariwal2020jukebox,
  title={Jukebox: A generative model for music},
  author={Dhariwal, Prafulla and Jun, Heewoo and Payne, Christine and Kim, Jong Wook and Radford, Alec and Sutskever, Ilya},
  journal={arXiv preprint arXiv:2005.00341},
  year={2020}
}
'''
    tags = [generation, vq_vae]
    abstract = '''We introduce Jukebox, a model that generates music with singing in the raw audio domain. We tackle the long context of raw audio using a multi-scale VQ-VAE to compress it to discrete codes, and modeling those using autoregressive Transformers. We show that the combined model at scale can generate high-fidelity and diverse songs with coherence up to multiple minutes. We can condition on artist and genre to steer the musical and vocal style, and on unaligned lyrics to make the singing more controllable. We are releasing thousands of non cherry-picked samples at this https URL, along with model weights and code at this https URL'''
    my_notes = '''
Transformer over VQ-VAE. Supervised with lyrics as condition. 
'''

class SPICE:
    apa = 'Gfeller, B., Frank, C., Roblek, D., Sharifi, M., Tagliasacchi, M., & Velimirović, M. (2020). SPICE: Self-supervised pitch estimation. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 28, 1118-1128.'
    bib = '''@article{gfeller2020spice,
  title={SPICE: Self-supervised pitch estimation},
  author={Gfeller, Beat and Frank, Christian and Roblek, Dominik and Sharifi, Matt and Tagliasacchi, Marco and Velimirovi{\'c}, Mihajlo},
  journal={IEEE/ACM Transactions on Audio, Speech, and Language Processing},
  volume={28},
  pages={1118--1128},
  year={2020},
  publisher={IEEE}
}
'''
    abstract = '''We propose a model to estimate the fundamental frequency in monophonic audio, often referred to as pitch estimation. We acknowledge the fact that obtaining ground truth annotations at the required temporal and frequency resolution is a particularly daunting task. Therefore, we propose to adopt a self-supervised learning technique, which is able to estimate pitch without any form of supervision. The key observation is that pitch shift maps to a simple translation when the audio signal is analysed through the lens of the constant-Q transform (CQT). We design a self-supervised task by feeding two shifted slices of the CQT to the same convolutional encoder, and require that the difference in the outputs is proportional to the corresponding difference in pitch. In addition, we introduce a small model head on top of the encoder, which is able to determine the confidence of the pitch estimate, so as to distinguish between voiced and unvoiced audio. Our results show that the proposed method is able to estimate pitch at a level of accuracy comparable to fully supervised models, both on clean and noisy audio samples, although it does not require access to large labeled datasets.'''
    tags = [self_supervise, f0, pitch_shift_invariance]
    my_notes = '''
This works??? What the heck
'''

class improving_music_performance_assessment_with_contrastive_learning:
    apa = 'Seshadri, P., & Lerch, A. (2021). Improving Music Performance Assessment with Contrastive Learning. arXiv preprint arXiv:2108.01711.'
    bib = '''@article{seshadri2021improving,
  title={Improving Music Performance Assessment with Contrastive Learning},
  author={Seshadri, Pavan and Lerch, Alexander},
  journal={arXiv preprint arXiv:2108.01711},
  year={2021}
}
'''
    abstract = '''Several automatic approaches for objective music performance assessment (MPA) have been proposed in the past, however, existing systems are not yet capable of reliably predicting ratings with the same accuracy as professional judges. This study investigates contrastive learning as a potential method to improve existing MPA systems. Contrastive learning is a widely used technique in representation learning to learn a structured latent space capable of separately clustering multiple classes. It has been shown to produce state of the art results for image-based classification problems. We introduce a weighted contrastive loss suitable for regression tasks applied to a convolutional neural network and show that contrastive loss results in performance gains in regression tasks for MPA. Our results show that contrastive-based methods are able to match and exceed SoTA performance for MPA regression tasks by creating better class clusters within the latent space of the neural networks.
'''
    tags = [contrastive]
    my_notes = ''

class PianoTouch:
    apa = 'Huang, K., Do, E. Y. L., & Starner, T. (2008, September). PianoTouch: A wearable haptic piano instruction system for passive learning of piano skills. In 2008 12th IEEE international symposium on wearable computers (pp. 41-44). IEEE.'
    bib = '''@inproceedings{huang2008pianotouch,
  title={PianoTouch: A wearable haptic piano instruction system for passive learning of piano skills},
  author={Huang, Kevin and Do, Ellen Yi-Luen and Starner, Thad},
  booktitle={2008 12th IEEE international symposium on wearable computers},
  pages={41--44},
  year={2008},
  organization={IEEE}
}
'''
    abstract = '''We present PianoTouch, a wearable, wireless haptic piano instruction system, composed of (1) five small vibration motors, one for each finger, fitted inside a glove, (2) a Bluetooth module mounted on the glove, and (3) piano music output from a laptop. Users hear the piano music and feel the vibrations indicating which finger is used to play the note. We investigate the system's potential for passive learning, i.e. learning piano playing automatically while engaged in everyday activities. In a preliminary study, four subjects learned two songs initially and then wore the PianoTouch glove for 30 minutes while listening to the songs repeated. One of the songs included tactile sensations and the other did not. The study found that after 30 minutes, the PianoTouch subjects were able to play the song accompanied by tactile sensations better than the non-tactile song. These results suggest the value of a more detailed study.
'''
    tags = [haptic, vibration, passive_learning, music_edu]
    my_notes = '''
Summary: user testing shows passive vibration input helps retain a song after learning it first. 
Q: During active learning, was there a score? During testing, was there a score? 
'''

class developing_a_haptic_glove_for_basic_piano_education:
    apa = 'Pala, F. K. (2019). Developing a haptic glove for basic piano education. World Journal on Educational Technology: Current Issues, 11(1), 38-47.'
    bib = '''@article{pala2019developing,
  title={Developing a haptic glove for basic piano education},
  author={Pala, Ferhat Kadir and others},
  journal={World Journal on Educational Technology: Current Issues},
  volume={11},
  number={1},
  pages={38--47},
  year={2019}
}
'''
    tags = [haptic, music_edu]
    my_notes = 'Hardly a good paper.'

class visiohaptic_trace_shape_longterm:
    apa = 'Yang, X. D., Bischof, W. F., & Boulanger, P. (2008, March). Validating the performance of haptic motor skill training. In 2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems (pp. 129-135). IEEE.'
    bib = '''@inproceedings{yang2008validating,
  title={Validating the performance of haptic motor skill training},
  author={Yang, Xing-Dong and Bischof, Walter F and Boulanger, Pierre},
  booktitle={2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems},
  pages={129--135},
  year={2008},
  organization={IEEE}
}
'''
    abstract = '''The effect of haptic interfaces on motor skill training has been widely studied. However, relatively little is known about whether haptic training can promote long-term motor skill acquisition. In this paper, we report two experimental studies that investigated the effectiveness of visuohaptic (visual + haptic) interfaces in helping people develop short-term and long-term motor skills. Our first study compared training outcomes of visuohaptic training, visual training, and no-assistance training. We found that the training outcomes for the tested methods were similar when helping participants develop short-term motor skills. Our second experiment assessed the potential of visual training and visuohaptic training in promoting the development of long-term motor skills. Participants were trained during a four-day-long period. The results showed that the participants gained long-term skills through both training methods, and that the training outcomes for both methods were similar. The results also showed that visuohaptic training is a promising method, but that it needs to be further developed to be useful.'''
    tags = [haptic, visual, multimodal, adaptive_curriculum_scaffolding]
    my_notes = '''
Maybe: 
    making a mistake and being corrected does not backprop.
    only actively correcting one's mistake backprops. 
paper: 
    passive learning -> less effort -> learn less
    "dynamically modify guidance ... according to the learner's skill level."
- Their visual is CYP overlaid onto ground truth. 
'''

class drum_haptic_audio:
    apa = 'Grindlay, G. (2008, March). Haptic guidance benefits musical motor learning. In 2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems (pp. 397-404). IEEE.'
    bib = '''@inproceedings{grindlay2008haptic,
  title={Haptic guidance benefits musical motor learning},
  author={Grindlay, Graham},
  booktitle={2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems},
  pages={397--404},
  year={2008},
  organization={IEEE}
}
'''
    abstract = '''This paper presents the results of a pilot experiment looking at the effect of haptic guidance on musical training. A percussion performance task was used where subjects learned to play short rhythmic sequences on a device capable of recording drumstick movements with a high degree of spatiotemporal accuracy. Subjects learned to perform the sequences under three primary training paradigms: listening to the rhythm (audio), being guided through the motions involved in the rhythm's performance (haptic), and being guided through the required motions while listening to the resulting sound (audio+haptic). Performance was assessed in terms of both timing and loudness (velocity) accuracy using several different metrics. Results indicate that haptic guidance can significantly benefit recall of both note timing and velocity. When subject performance was compared in terms of note velocity recall, the addition of haptic guidance to audio-based training produced a 17% reduction in final error when compared to audio training alone. When performance was evaluated in terms of liming recall, the combination of audio and haptic guidance led to an 18% reduction in early-stage error.'''
    tags = [haptic, audio, multimodal, music_edu]
    my_notes = '''Nice engineering and stats.'''

class three_d_trajectory_haptic:
    apa = 'Feygin, D., Keehner, M., & Tendick, R. (2002, March). Haptic guidance: Experimental evaluation of a haptic training method for a perceptual motor skill. In Proceedings 10th Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems. HAPTICS 2002 (pp. 40-47). IEEE.'
    bib = '''@inproceedings{feygin2002haptic,
  title={Haptic guidance: Experimental evaluation of a haptic training method for a perceptual motor skill},
  author={Feygin, David and Keehner, Madeleine and Tendick, R},
  booktitle={Proceedings 10th Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems. HAPTICS 2002},
  pages={40--47},
  year={2002},
  organization={IEEE}
}
'''
    abstract = '''In this paper we investigate a use of haptics for skills training which we call haptic guidance. In the haptic guidance paradigm, the subject is physically guided through the ideal motion by the haptic interface, thus giving the subject a kinesthetic understanding of what is required. Subjects learned a complex 3D motion under three training conditions (haptic, visual, haptic and visual) and were required to manually reproduce the movement under two recall conditions (with vision, without vision). Performance was measured in terms of position, shape, timing, and drift. Findings from this study indicate that haptic guidance is effective in training. While visual training was better for teaching the trajectory shape, temporal aspects of the task were more effectively learned from haptic guidance. This supports a possible role for haptics in the training of perceptual motor skills in virtual environments.'''
    tags = [haptic, visual, multimodal]
    my_notes = '''
Cite: 
    haptic guidance: "the subject is physically guided through the ideal motion by the haptic interface, thus giving the subject a kinesthetic understanding of what is required."
- abstract highlight: H is better for rhythm and V for trajectory. 
- Their visual is only ground truth, no interactivity. 
- 学 H (眼睛遮住) 测 H+V (眼睛睁开) 的分数比 测 H (眼睛遮住) 分数低。"This suggests that vision may somehow interfere with the haptic representation of the task."
Q: 为什么 V training phase 只是观察 ground truth, 没有同时动手？这才导致了 V vs H 与 observation vs practice 耦合了？
'''

class MoveMe_haptic_guide_theremin:
    apa = 'Fujii, K., Russo, S. S., Maes, P., & Rekimoto, J. (2015, November). MoveMe: 3D haptic support for a musical instrument. In Proceedings of the 12th International Conference on Advances in Computer Entertainment Technology (pp. 1-8).'
    bib = '''@inproceedings{fujii2015moveme,
  title={MoveMe: 3D haptic support for a musical instrument},
  author={Fujii, Katsuya and Russo, Sophia S and Maes, Pattie and Rekimoto, Jun},
  booktitle={Proceedings of the 12th International Conference on Advances in Computer Entertainment Technology},
  pages={1--8},
  year={2015}
}
'''
    abstract = '''Fine motor skills like finger/hand manipulations are essential for playing musical instruments and these skills require a great amount of time and effort to acquire. Researchers have been introducing haptic feedback systems in order to facilitate the process of learning motor skills but little research has expanded the possibility of applying to the field of musical instruments. Hence, we developed a system called "MoveMe" that provides three-dimensional haptic support for playing a musical instrument. The system guides a user's hands as if someone else was holding their hands to help a beginner play a musical instrument. With the system, an expert can pre-record his/her movements so that a beginner can play it back later as necessary. Alternatively, the system connects an expert and a beginner via two haptic robots and the expert can, in real time, guide and correct the beginner's movement. In addition to those functionalities, we introduce a new proficiency metric provided by force feedback. A master can evaluate how much a beginner has improved using both audio feedback as well as this new force-based metric. Through the experiments that we conducted, we found that our system is effective in terms of playing a song at a correct speed and rhythm.
'''
    tags = [haptic, music_edu]

class vibro_tactile_drum:
    apa = 'Tom, A., Singh, A., Daigle, M., Marandola, F., & Wanderley, M. (2020). Haptic Tutor-A haptics-based music education tool for beginners. In International Workshop on Haptic and Audio Interaction Design.'
    bib = '''@inproceedings{tom2020haptic,
  title={Haptic Tutor-A haptics-based music education tool for beginners},
  author={Tom, Ajin and Singh, Ankita and Daigle, Martin and Marandola, Fabrice and Wanderley, Marcelo},
  booktitle={International Workshop on Haptic and Audio Interaction Design},
  year={2020}
}
'''
    abstract = '''In this paper we introduce Haptic Tutor, a wearable haptic system for triggering vibrations on limbs of a student drummer aimed to help develop multi-limb independence. The system uses portable, wireless vibrotactile devices to display haptic information on drummers' limbs. To asses the usefulness of the system, we analyse response time differences between stimuli and motor action (drum stroke). Our hypotheses are that the use of haptic stimuli will improve the temporal characteristics of performances, but also that the type of haptic stimuli will have an influence on performance results. To validate these hypotheses we conducted two experiments. The first one with participants randomly distributed in three groups, each group performing simple drumming lessons involving both hands under a given condition (no haptics, haptic pulse and haptic ramp). Results show clear improvement in strike accuracy for both haptic conditions, most clearly in the haptic ramp condition. Using these results, a second experiment was carried out in which 6 other participants were randomly divided into two groups (no haptics and haptic ramp conditions) and asked to perform a more complex lesson, this time involving three limbs (two arms and right foot). Results of both experiments show clear improvement on strike accuracy (reduced asynchrony), but a less important difference on strike precision (inter-onset-interval deviation) for the haptic condition. We finally report on participants subjective comments , discussing the limitations of the current prototype.'''
    tags = [haptic, music_edu, vibration]

class scaffolding:
    apa = 'Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. Journal of child psychology and psychiatry, 17(2), 89-100.'
    bib = '''@article{wood1976role,
  title={The role of tutoring in problem solving},
  author={Wood, David and Bruner, Jerome S and Ross, Gail},
  journal={Journal of child psychology and psychiatry},
  volume={17},
  number={2},
  pages={89--100},
  year={1976},
  publisher={Wiley Online Library}
}
'''
    abstract = None
    tags = [adaptive_curriculum_scaffolding]
    my_notes = '''
This paper proposed "scaffolding". 
scaffolding: focus on what little you can learn at the moment and leave the unlearnable to the tutor's assistance. 
I think: learn one thing at a time. 
'''

class fading_scaffold:
    apa = "McNeill, K. L., Lizotte, D. J., Krajcik, J., & Marx, R. W. (2006). Supporting students' construction of scientific explanations by fading scaffolds in instructional materials. The Journal of the Learning Sciences, 15(2), 153-191."
    bib = '''@article{mcneill2006supporting,
  title={Supporting students' construction of scientific explanations by fading scaffolds in instructional materials},
  author={McNeill, Katherine L and Lizotte, David J and Krajcik, Joseph and Marx, Ronald W},
  journal={The Journal of the Learning Sciences},
  volume={15},
  number={2},
  pages={153--191},
  year={2006},
  publisher={Taylor \& Francis}
}
'''
    abstract = '''The purpose of this study was to determine whether providing students with continuous written instructional support or fading written instructional support (scaffolds) better prepares students to construct scientific explanations when they are no longer provided with support. This article investigated the influence of scaffolding on 331 seventh-grade students' writing of scientific explanations during an 8-week, project-based chemistry unit in which the construction of scientific explanations is a key learning goal. The unit makes an instructional model for explanation explicit to students through a focal lesson and reinforces that model through subsequent written support for each investigation. Students received 1 of 2 treatments in terms of the type of written support: continuous, involving detailed support for every investigation, or faded, involving less support over time. The analyses showed significant learning gains for students for all components of scientific explanation (i.e., claim, evidence, and reasoning). However, on posttest items lacking scaffolds, the faded group gave stronger explanations in terms of their reasoning compared to the continuous group. Fading written scaffolds better equipped students to write explanations when they were not provided with support.'''
    tags = [adaptive_curriculum_scaffolding]
    my_notes = '''fading scaffold'''

class xcp:
    apa = 'Katabi, D., Handley, M., & Rohrs, C. (2002, August). Congestion control for high bandwidth-delay product networks. In Proceedings of the 2002 conference on Applications, technologies, architectures, and protocols for computer communications (pp. 89-102).'
    bib = '''@inproceedings{katabi2002congestion,
  title={Congestion control for high bandwidth-delay product networks},
  author={Katabi, Dina and Handley, Mark and Rohrs, Charlie},
  booktitle={Proceedings of the 2002 conference on Applications, technologies, architectures, and protocols for computer communications},
  pages={89--102},
  year={2002}
}
'''
    abstract = '''Theory and experiments show that as the per-flow product of bandwidth and latency increases, TCP becomes inefficient and prone to instability, regardless of the queuing scheme. This failing becomes increasingly important as the Internet evolves to incorporate very high-bandwidth optical links and more large-delay satellite links.To address this problem, we develop a novel approach to Internet congestion control that outperforms TCP in conventional environments, and remains efficient, fair, scalable, and stable as the bandwidth-delay product increases. This new eXplicit Control Protocol, XCP, generalizes the Explicit Congestion Notification proposal (ECN). In addition, XCP introduces the new concept of decoupling utilization control from fairness control. This allows a more flexible and analytically tractable protocol design and opens new avenues for service differentiation.Using a control theory framework, we model XCP and demonstrate it is stable and efficient regardless of the link capacity, the round trip delay, and the number of sources. Extensive packet-level simulations show that XCP outperforms TCP in both conventional and high bandwidth-delay environments. Further, XCP achieves fair bandwidth allocation, high utilization, small standing queue size, and near-zero packet drops, with both steady and highly varying traffic. Additionally, the new protocol does not maintain any per-flow state in routers and requires few CPU cycles per packet, which makes it implementable in high-speed routers.'''
    tags = [network]
    my_notes = '''
The router knows both the spare bandwidth and the queue. 
    THe routers mark the packets. 
Uses control theory to ensure stablity. 
'''

class deep_emb_helps_segmentation:
    apa = 'Salamon, J., Nieto, O., & Bryan, N. J. (2017). Deep Embeddings and Section Fusion Improve Music Segmentation. IEEE Signal Processing Letters, 24(3), 279-283.'
    bib = '''@article{salamon2017deep,
  title={Deep Embeddings and Section Fusion Improve Music Segmentation},
  author={Salamon, Justin and Nieto, Oriol and Bryan, Nicholas J},
  journal={IEEE Signal Processing Letters},
  volume={24},
  number={3},
  pages={279--283},
  year={2017}
}
'''
    abstract = '''Music segmentation algorithms identify the structure of a music recording by automatically dividing it into sections and determining which sections repeat and when. Since the desired granularity of the sections may vary by application, multi-level segmentation produces several levels of segmentation ordered by granularity from one section (the whole song) up to N unique sections, and has proven to be a challenging MIR task. In this work we propose a multi-level segmentation method that leverages deep audio embeddings learned via other tasks. Our approach builds on an existing multi-level segmentation algorithm, replacing manually engineered features with deep embeddings learned through audio classification problems where data are abundant. Additionally, we propose a novel section fusion algorithm that leverages the multi-level segmentation to consolidate short segments at each level in a way that is consistent with the segmentations at lower levels. Through a series of experiments we show that replacing handcrafted features with deep embeddings can lead to significant improvements in multilevel music segmentation performance, and that section fusion further improves the results by cleaning up spurious short sections. We compare our approach to two strong baselines and show that it yields state-of-the-art results.'''
    tags = [hierarchical, time_hierarchy]
    my_notes = '''See slides at https://docs.google.com/presentation/d/143vXGAh7HiYN-WrxxkjLaHpi0NWK_2Md/edit?usp=sharing&ouid=111628173406875267677&rtpof=true&sd=true
Using deep emb to segmentate audio. 
No finetuning. Using existing clustering algo on deep emb. 
'''

class implementing_a_generative_theory_of_tonal_music:
    apa = 'Hamanaka, M., Hirata, K., & Tojo, S. (2006). Implementing “A generative theory of tonal music”. Journal of New Music Research, 35(4), 249-277.'
    bib = '''@article{hamanaka2006implementing,
  title={Implementing “A generative theory of tonal music”},
  author={Hamanaka, Masatoshi and Hirata, Keiji and Tojo, Satoshi},
  journal={Journal of New Music Research},
  volume={35},
  number={4},
  pages={249--277},
  year={2006},
  publisher={Taylor \& Francis}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
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
'''

class deepGTTM_I_II_local_boundary_and_metrical_structure_analyzer_based_on_deep_learning:
    apa = 'Hamanaka, M., Hirata, K., & Tojo, S. (2016, July). deepGTTM-I&II: Local boundary and metrical structure analyzer based on deep learning technique. In International Symposium on Computer Music Multidisciplinary Research (pp. 3-21). Springer, Cham.'
    bib = '''@inproceedings{hamanaka2016deepgttm,
  title={deepGTTM-I\&II: Local boundary and metrical structure analyzer based on deep learning technique},
  author={Hamanaka, Masatoshi and Hirata, Keiji and Tojo, Satoshi},
  booktitle={International Symposium on Computer Music Multidisciplinary Research},
  pages={3--21},
  year={2016},
  organization={Springer}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
8-bar monophonic.  
The output of the NN is not only the metrical structure, 
but also the applicability of GTTM rules on each note.  
The input has manually annotated grouping structure.  
    not sure. maybe a part of curriculum.  
NN is many FC layers.  
Misc. 
    Related work "FATTA" [3] can be baseline, but monophonic.  
'''

class music_structural_analysis_database_based_on_GTTM:
    apa = 'Hamanaka, M., Hirata, K., & Tojo, S. (2014). Musical structural analysis database based on GTTM.'
    bib = '''@article{hamanaka2014musical,
  title={Musical structural analysis database based on GTTM},
  author={Hamanaka, Masatoshi and Hirata, Keiji and Tojo, Satoshi},
  year={2014},
  publisher={ISMIR 2014}
}'''
    tags = [lit_review_for_junyan_ismir_2022, dataset]
    my_notes = '''
A dataset of GTTM-annotated monophonic pieces, each ~ 8 bars.  
'''

class deepGTTM_III_simultaneous_learning_of_grouping_and_metrical_structures:
    apa = 'Hirata, M. H. K., & Tojo, S. deepGTTM-III: Simultaneous Learning of Grouping and Metrical Structures.'
    bib = '''@article{hiratadeepgttm,
  title={deepGTTM-III: Simultaneous Learning of Grouping and Metrical Structures},
  author={Hirata, Masatoshi Hamanaka1 Keiji and Tojo, Satoshi}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Include feedback between metrical and grouping structures.  
In practice, it's just multi-task learning using shared 
backbones.  
'''

class searching_for_metric_structure_of_musical_files:
    apa = 'Kostek, B., Wojcik, J., & Szczuko, P. (2007, June). Searching for Metric Structure of Musical Files. In International Conference on Rough Sets and Intelligent Systems Paradigms (pp. 774-783). Springer, Berlin, Heidelberg.'
    bib = '''@inproceedings{kostek2007searching,
  title={Searching for Metric Structure of Musical Files},
  author={Kostek, Bozena and Wojcik, Jaroslaw and Szczuko, Piotr},
  booktitle={International Conference on Rough Sets and Intelligent Systems Paradigms},
  pages={774--783},
  year={2007},
  organization={Springer}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Symbolic polyphonic -> ANN -> note accented or not.  
Only one level of metrical struct.  
'''

class machine_rhythm_computer_emulation_of_human_rhythm_perception:
    apa = 'Rosenthal, D. F. (1992). Machine rhythm--computer emulation of human rhythm perception (Doctoral dissertation, Massachusetts Institute of Technology).'
    bib = '''@phdthesis{rosenthal1992machine,
  title={Machine rhythm--computer emulation of human rhythm perception},
  author={Rosenthal, David Felix},
  year={1992},
  school={Massachusetts Institute of Technology}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Symbolic polyphonic -> "Machine Rhythm" 
-> 3-level rhythmic annotation  
A 1977 PhD thesis. So probably you can't get their code.  
'''

class modeling_meter_and_harmony_a_preference_rule_approach:
    apa = 'Temperley, D., & Sleator, D. (1999). Modeling meter and harmony: A preference-rule approach. Computer Music Journal, 23(1), 10-27.'
    bib = '''@article{temperley1999modeling,
  title={Modeling meter and harmony: A preference-rule approach},
  author={Temperley, David and Sleator, Daniel},
  journal={Computer Music Journal},
  volume={23},
  number={1},
  pages={10--27},
  year={1999},
  publisher={JSTOR}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
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
'''

class inferring_metrical_structure_in_music_using_particle_filters:
    apa = 'Krebs, F., Holzapfel, A., Cemgil, A. T., & Widmer, G. (2015). Inferring metrical structure in music using particle filters. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 23(5), 817-827.'
    bib = '''@article{krebs2015inferring,
  title={Inferring metrical structure in music using particle filters},
  author={Krebs, Florian and Holzapfel, Andre and Cemgil, Ali Taylan and Widmer, Gerhard},
  journal={IEEE/ACM Transactions on Audio, Speech, and Language Processing},
  volume={23},
  number={5},
  pages={817--827},
  year={2015},
  publisher={IEEE}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
non symbolic -> 2-level metrical struct
'''

class gtsim_a_computer_simulation_of_music_perception:
    apa = 'Jones, J., Scarborough, D., & Miller, B. (1993). Gtsim a computer simulation of music perception. Computers and the Humanities, 27(1), 19-23.'
    bib = '''@article{jones1993gtsim,
  title={Gtsim a computer simulation of music perception},
  author={Jones, Jacqueline and Scarborough, Don and Miller, Benjamin},
  journal={Computers and the Humanities},
  volume={27},
  number={1},
  pages={19--23},
  year={1993},
  publisher={Springer}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Work in progress from 1993...  
'''

class on_hierarchical_clustering_of_spectrogram:
    apa = 'Sawada, S., Takegawa, Y., & Hirata, K. (2017, September). On Hierarchical Clustering of Spectrogram. In International Symposium on Computer Music Multidisciplinary Research (pp. 226-237). Springer, Cham.'
    bib = '''@inproceedings{sawada2017hierarchical,
  title={On Hierarchical Clustering of Spectrogram},
  author={Sawada, Shun and Takegawa, Yoshinari and Hirata, Keiji},
  booktitle={International Symposium on Computer Music Multidisciplinary Research},
  pages={226--237},
  year={2017},
  organization={Springer}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
spectrogram -> grouping struct  
Looks like a good paper, but so hard to read.  
没读完.  
'''

class a_constraint_based_approach_to_grouping_in_language_and_music:
    apa = 'van der Werf, S., & Hendriks, P. (2004). A constraint-based approach to grouping in language and music. In Proceedings: First Conference on Interdisciplinary Musicology CIM04, Graz, Austria.'
    bib = '''@inproceedings{van2004constraint,
  title={A constraint-based approach to grouping in language and music},
  author={van der Werf, Sybrand and Hendriks, Petra},
  booktitle={Proceedings: First Conference on Interdisciplinary Musicology CIM04, Graz, Austria},
  year={2004}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
GTTM -> OT (optimality theory).  
Gives a parser for symbolic monophonic short pieces.  
Compares with human annotations.  
Parser is based on the magic of Prolog.  
'''

class a_rule_based_expert_system_for_music_perception:
    apa = 'Jones, J. A., Miller, B. O., & Scarborough, D. L. (1988). A rule-based expert system for music perception. Behavior Research Methods, Instruments, & Computers, 20(2), 255-262.'
    bib = '''@article{jones1988rule,
  title={A rule-based expert system for music perception},
  author={Jones, Jacqueline A and Miller, Benjamin O and Scarborough, Don L},
  journal={Behavior Research Methods, Instruments, \& Computers},
  volume={20},
  number={2},
  pages={255--262},
  year={1988},
  publisher={Springer}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
monophonic symbolic -> 6-level metrical struct  
1988 的在读 PhD 搞的， 估计要不来 source code.  
Rule-based. Does not *seem* to consider PR, only WFR.  
'''

class a_theoretical_framework_for_rhythm_perception:
    apa = 'Povel, D. J. (1984). A theoretical framework for rhythm perception. Psychological research, 45(4), 315-337.'
    bib = '''@article{povel1984theoretical,
  title={A theoretical framework for rhythm perception},
  author={Povel, Dirk-Jan},
  journal={Psychological research},
  volume={45},
  number={4},
  pages={315--337},
  year={1984},
  publisher={Springer}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Proposes grid theory.  
"Pre-GTTM" simple theory to parse simple rhythm.  
'''

class perception_of_temporal_patterns:
    apa = 'Povel, D. J., & Essens, P. (1985). Perception of temporal patterns. Music perception, 2(4), 411-440.'
    bib = '''@article{povel1985perception,
  title={Perception of temporal patterns},
  author={Povel, Dirk-Jan and Essens, Peter},
  journal={Music perception},
  volume={2},
  number={4},
  pages={411--440},
  year={1985},
  publisher={University of California Press}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Another non-GTTM rhythm perception theory.  
It's more or less a 2-level struct.  
Proposes an algo too.  
'''

class a_review_of_automatic_rhythm_description_systems:
    apa = 'Gouyon, F., & Dixon, S. (2005). A review of automatic rhythm description systems. Computer music journal, 29(1), 34-54.'
    bib = '''@article{gouyon2005review,
  title={A review of automatic rhythm description systems},
  author={Gouyon, Fabien and Dixon, Simon},
  journal={Computer music journal},
  volume={29},
  number={1},
  pages={34--54},
  year={2005},
  publisher={JSTOR}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
A lit review of many rhythm trackers.  
Notes the commonality of their methods.  
However, seems to emphasize only levels 0:3.  
Also input is non-symbolic audio.  
Section "Time Signature Determination" is useful.  
'''

class a_hybrid_graphical_model_for_rhythmic_parsing:
    apa = 'Raphael, C. (2002). A hybrid graphical model for rhythmic parsing. Artificial Intelligence, 137(1-2), 217-238.'
    bib = '''@article{raphael2002hybrid,
  title={A hybrid graphical model for rhythmic parsing},
  author={Raphael, Christopher},
  journal={Artificial Intelligence},
  volume={137},
  number={1-2},
  pages={217--238},
  year={2002},
  publisher={Elsevier}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
symbolic -> rhythm parse  
method: ???  
'''

class robust_downbeat_tracking_using_an_ensemble_of_convolutional_networks:
    apa = 'Durand, S., Bello, J. P., David, B., & Richard, G. (2016). Robust downbeat tracking using an ensemble of convolutional networks. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 25(1), 76-89.'
    bib = '''@article{durand2016robust,
  title={Robust downbeat tracking using an ensemble of convolutional networks},
  author={Durand, Simon and Bello, Juan Pablo and David, Bertrand and Richard, Ga{\"e}l},
  journal={IEEE/ACM Transactions on Audio, Speech, and Language Processing},
  volume={25},
  number={1},
  pages={76--89},
  year={2016},
  publisher={IEEE}
}'''
    tags = [lit_review_for_junyan_ismir_2022]

class a_generalized_bayesian_model_for_tracking_long_metrical_cycles_in_acoustic_music_signals:
    apa = 'Srinivasamurthy, A., Holzapfel, A., Cemgil, A. T., & Serra, X. (2016, March). A generalized bayesian model for tracking long metrical cycles in acoustic music signals. In 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 76-80). IEEE.'
    bib = '''@inproceedings{srinivasamurthy2016generalized,
  title={A generalized bayesian model for tracking long metrical cycles in acoustic music signals},
  author={Srinivasamurthy, Ajay and Holzapfel, Andre and Cemgil, Ali Taylan and Serra, Xavier},
  booktitle={2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={76--80},
  year={2016},
  organization={IEEE}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Meter tracking improved for non-western music where each bar 
is very long.  
'''

class automatic_salience_based_hypermetric_rhythm_retrieval:
    apa = "Kostek, B., & Wojcik, J. (2007, April). Automatic salience-based hypermetric rhythm retrieval. In 2007 International Conference on Multimedia and Ubiquitous Engineering (MUE'07) (pp. 1220-1226). IEEE."
    bib = '''@inproceedings{kostek2007automatic,
  title={Automatic salience-based hypermetric rhythm retrieval},
  author={Kostek, Bozena and Wojcik, Jaroslaw},
  booktitle={2007 International Conference on Multimedia and Ubiquitous Engineering (MUE'07)},
  pages={1220--1226},
  year={2007},
  organization={IEEE}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
整篇一直在说 hypermetric rhythm, 但整篇没看到。  
'''

class a_unified_probabilistic_model_for_polyphonic_music_analysis:
    apa = 'Temperley, D. (2009). A unified probabilistic model for polyphonic music analysis. Journal of New Music Research, 38(1), 3-18.'
    bib = '''@article{temperley2009unified,
  title={A unified probabilistic model for polyphonic music analysis},
  author={Temperley, David},
  journal={Journal of New Music Research},
  volume={38},
  number={1},
  pages={3--18},
  year={2009},
  publisher={Taylor \& Francis}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
polyphonic symbolic -> metrical + harmonic + stream struct  
Open source at http://www.theory.esm.rochester/  
Generative -- Bayesian -> analytical  
The metrical rules are more strict than GTTM, only giving 
very regular parses.  
'''

class determination_of_the_meter_of_musical_scores_by_autocorrelation:
    apa = 'Brown, J. C. (1993). Determination of the meter of musical scores by autocorrelation. The Journal of the Acoustical Society of America, 94(4), 1953-1957.'
    bib = '''@article{brown1993determination,
  title={Determination of the meter of musical scores by autocorrelation},
  author={Brown, Judith C},
  journal={The Journal of the Acoustical Society of America},
  volume={94},
  number={4},
  pages={1953--1957},
  year={1993},
  publisher={Acoustical Society of America}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Assumes more notes are at downbeats than at upbeats.  
Trivially, autocorrelation can expose the meter.  
No pitch, only onsets.  
'''

class automatic_meter_extraction_from_midi_files:
    apa = "Meudic, B. (2002, June). Automatic meter extraction from MIDI files. In Journées d'informatique musicale (pp. 1-1)."
    bib = '''@inproceedings{meudic2002automatic,
  title={Automatic meter extraction from MIDI files},
  author={Meudic, Benoit},
  booktitle={Journ{\'e}es d'informatique musicale},
  pages={1--1},
  year={2002}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
symbolic polyphonic -> 4-level metrical struct  
No link to source code. Ask authors.  
The main goal is to infer the meter.  
Method is auto-correlation.  
'''

class finding_meter_in_music_using_an_autocorrelation_phase_matrix_and_shannon_entropy:
    apa = 'Eck, D., & Casagrande, N. (2005). Finding meter in music using an autocorrelation phase matrix and shannon entropy. Target, 300(350), 400.'
    bib = '''@article{eck2005finding,
  title={Finding meter in music using an autocorrelation phase matrix and shannon entropy},
  author={Eck, Douglas and Casagrande, Norman},
  journal={Target},
  volume={300},
  number={350},
  pages={400},
  year={2005}
}'''
    tags = [lit_review_for_junyan_ismir_2022]

class meter_detection_in_symbolic_music_using_inner_metric_analysis:
    apa = 'De Haas, W. B., & Volk, A. (2016, August). Meter detection in symbolic music using inner metric analysis. In International Society for Music Information Retrieval Conference (p. 441).'
    bib = '''@inproceedings{de2016meter,
  title={Meter detection in symbolic music using inner metric analysis},
  author={De Haas, W Bas and Volk, Anja},
  booktitle={International Society for Music Information Retrieval Conference},
  pages={441},
  year={2016}
}'''
    tags = [lit_review_for_junyan_ismir_2022]

class automatic_generation_of_grouping_structure_based_on_the_gttm:
    apa = 'Hamanaka, M., Hirata, K., & Tojo, S. (2004, November). Automatic Generation of Grouping Structure based on the GTTM. In ICMC.'
    bib = '''@inproceedings{hamanaka2004automatic,
  title={Automatic Generation of Grouping Structure based on the GTTM},
  author={Hamanaka, Masatoshi and Hirata, Keiji and Tojo, Satoshi},
  booktitle={ICMC},
  year={2004}
}'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Looks just like ATTA.  
'''

class beat_and_downbeat_tracking_of_symbolic_music_data_using_deep_recurrent_neural_networks:
    apa = 'Chuang, Y. C., & Su, L. (2020, December). Beat and downbeat tracking of symbolic music data using deep recurrent neural networks. In 2020 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC) (pp. 346-352). IEEE.'
    bib = '''@inproceedings{chuang2020beat,
  title={Beat and downbeat tracking of symbolic music data using deep recurrent neural networks},
  author={Chuang, Yi-Chin and Su, Li},
  booktitle={2020 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC)},
  pages={346--352},
  year={2020},
  organization={IEEE}
}'''
    abstract = '''Musical beat tracking is one of the most investigated tasks in music information retrieval (MIR). Research endeavors on this task have mostly been focused on the modeling of audio data representations. In contrast, beat tracking of symbolic music contents (e.g., MIDI, score sheets) has been relatively overlooked in the past years. In this paper, we revisit the task of symbolic music beat tracking and present to solve this task with modern deep learning approaches. To the extent of our knowledge, it is the first time that utilizing deep learning approaches to track beats and downbeats of symbolic music data. The proposed symbolic beat tracking framework performs joint beat and downbeat tracking in a multi-task learning (MTL) manner, and we investigate various types of networks which are based on the recurrent neural networks (RNN), such as bidirectional long short-term memory (BLSTM) network, hierarchical multi-scale (HM) LSTM, and BLSTM with the attention mechanism. In the experiments, a systematic comparison of these networks and state-of-art audio beat tracking methods are performed on the MusicNet dataset. Experiment results show that the BLSTM model trained specifically on symbolic data outperforms the state-of-the-art beat tracking methods utilized on synthesized audio. Such a comparison of performance also indicates the technical challenges in symbolic music beat tracking.'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Double binary classification (beat? downbeat?) for each 
timestep.  
'''

class representations_of_music_in_ranking_rhythmic_hypotheses:
    apa = 'Wojcik, J., & Kostek, B. (2010). Representations of music in ranking rhythmic hypotheses. In Advances in Music Information Retrieval (pp. 39-64). Springer, Berlin, Heidelberg.'
    bib = '''@incollection{wojcik2010representations,
  title={Representations of music in ranking rhythmic hypotheses},
  author={Wojcik, Jaroslaw and Kostek, Bozena},
  booktitle={Advances in Music Information Retrieval},
  pages={39--64},
  year={2010},
  publisher={Springer}
}'''
    abstract = '''The chapter presents first the main issues related to music information retrieval (MIR) domain. Within this domain, there exists a variety of approaches to musical instrument recognition, musical phrase classification, melody classification (e.g. query-by-humming systems), rhythm retrieval, retrieval of high-level-musical features such as looking for emotions in music or differences in expressiveness, music search based on listeners’ preferences, etc. The objective of this study is to propose a method for retrieval of hypermetric rhythm on the basis of melody. A stream of sounds in MIDI format is introduced at the system input. On the basis of a musical content the method retrieves a hypermetric structure of rhythm of a musical piece consisting of rhythmic motives, phrases, and sentences. On the basis of the hypermetric structure retrieved, a system capable of creating automatic drum accompaniment to a given melody supporting the composition is proposed. A method does not use any information about rhythm (time signature), which is often included in MIDI information. Neither rhythmic tracks nor harmonic information are used in this method. The only information analyzed is a melody, which may be monophonic as well as polyphonic. The analysis starts after the entire piece has been played. Recurrence of melodic and rhythmic patterns and the rhythmic salience of sounds are combined to create an algorithm that finds the metric structure of rhythm in a given melody.'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Actually hypermeter parsing.  
"The objective of this study is to propose a method for 
retrieval of hypermetric rhythm on the basis of melody"  
Propose parses and rank them using rule-based.  
'''

class enhanced_hierarchical_music_structure_annotations_via_feature_level_similarity_fusion:
    apa = 'Tralie, C. J., & McFee, B. (2019, May). Enhanced hierarchical music structure annotations via feature level similarity fusion. In ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 201-205). IEEE.'
    bib = '''@inproceedings{tralie2019enhanced,
  title={Enhanced hierarchical music structure annotations via feature level similarity fusion},
  author={Tralie, Christopher J and McFee, Brian},
  booktitle={ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={201--205},
  year={2019},
  organization={IEEE}
}'''
    abstract = '''We describe a novel pipeline to automatically discover hierarchies of repeated sections in musical audio. The proposed method uses similarity network fusion (SNF) to combine different frame-level features into clean affinity matrices, which are then used as input to spectral clustering. While prior spectral clustering approaches to music structure analysis have pre-processed affinity matrices with heuristics specifically designed for this task, we show that the SNF approach directly yields segmentations which agree better with human annotators, as measured by the "L-measure" metric for hierarchical annotations. Furthermore, the SNF approach immediately supports arbitrarily many input features, allowing us to simultaneously discover structure encoded in timbral, harmonic, and rhythmic representations without any changes to the base algorithm.'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
SNF (similarity network fusion) can fuse multiple similarity 
metrics. Then, they use spectral clustering.  
'''

class unsupervised_music_structure_annotation_by_time_series_structure_features_and_segment_similarity:
    apa = 'Serra, J., Müller, M., Grosche, P., & Arcos, J. L. (2014). Unsupervised music structure annotation by time series structure features and segment similarity. IEEE Transactions on Multimedia, 16(5), 1229-1240.'
    bib = '''@article{serra2014unsupervised,
  title={Unsupervised music structure annotation by time series structure features and segment similarity},
  author={Serra, Joan and M{\"u}ller, Meinard and Grosche, Peter and Arcos, Josep Ll},
  journal={IEEE Transactions on Multimedia},
  volume={16},
  number={5},
  pages={1229--1240},
  year={2014},
  publisher={IEEE}
}'''
    abstract = '''Automatically inferring the structural properties of raw multimedia documents is essential in today's digitized society. Given its hierarchical and multi-faceted organization, musical pieces represent a challenge for current computational systems. In this article, we present a novel approach to music structure annotation based on the combination of structure features with time series similarity. Structure features encapsulate both local and global properties of a time series, and allow us to detect boundaries between homogeneous, novel, or repeated segments. Time series similarity is used to identify equivalent segments, corresponding to musically meaningful parts. Extensive tests with a total of five benchmark music collections and seven different human annotations show that the proposed approach is robust to different ground truth choices and parameter settings. Moreover, we see that it outperforms previous approaches evaluated under the same framework.'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
Intro has a nice review.  
Not only clustering, but also cut according to novelty peaks.  
我没读完。  
'''

class boundary_detection_in_music_structure_analysis_using_convolutional_neural_networks:
    apa = 'Ullrich, K., Schlüter, J., & Grill, T. (2014, October). Boundary Detection in Music Structure Analysis using Convolutional Neural Networks. In ISMIR (pp. 417-422).'
    bib = '''@inproceedings{ullrich2014boundary,
  title={Boundary Detection in Music Structure Analysis using Convolutional Neural Networks.},
  author={Ullrich, Karen and Schl{\"u}ter, Jan and Grill, Thomas},
  booktitle={ISMIR},
  pages={417--422},
  year={2014}
}'''
    abstract = '''The recognition of boundaries, e.g., between chorus andverse, is an important task in music structure analysis. Thegoal is to automatically detect such boundaries in audiosignals so that the results are close to human annotation.In this work, we apply Convolutional Neural Networks tothe task, trained directly on mel-scaled magnitude spectrograms. On a representative subset of the SALAMI structural annotation dataset, our method outperforms currenttechniques in terms of boundary retrieval F-measure at different temporal tolerances: We advance the state-of-the-artfrom 0.33 to 0.46 for tolerances of ±0.5 seconds, and from0.52 to 0.62 for tolerances of ±3 seconds. As the algorithm is trained on annotated audio data without the needof expert knowledge, we expect it to be easily adaptableto changed annotation guidelines and also to related taskssuch as the detection of song transitions.'''
    tags = [lit_review_for_junyan_ismir_2022]

class automatic_analysis_and_influence_of_hierarchical_structure_on_melody_rhythm_and_harmony_in_popular_music:
    apa = 'Dai, S., Zhang, H., & Dannenberg, R. B. (2020). Automatic analysis and influence of hierarchical structure on melody, rhythm and harmony in popular music. arXiv preprint arXiv:2010.07518.'
    bib = '''@article{dai2020automatic,
  title={Automatic analysis and influence of hierarchical structure on melody, rhythm and harmony in popular music},
  author={Dai, Shuqi and Zhang, Huan and Dannenberg, Roger B},
  journal={arXiv preprint arXiv:2010.07518},
  year={2020}
}'''
    abstract = '''Repetition is a basic indicator of musical structure. This study introduces new algorithms for identifying musical phrases based on repetition. Phrases combine to form sections yielding a two-level hierarchical structure. Automatically detected hierarchical repetition structures reveal significant interactions between structure and chord progressions, melody and rhythm. Different levels of hierarchy interact differently, providing evidence that structural hierarchy plays an important role in music beyond simple notions of repetition or similarity. Our work suggests new applications for music generation and music evaluation.'''
    tags = [lit_review_for_junyan_ismir_2022]
    my_notes = '''
First segment the song by minimizing SDL (Structure 
Description Length).  
'''

class hierarchical_motion_understanding_via_motion_programs:
    apa = 'Kulal, S., Mao, J., Aiken, A., & Wu, J. (2021). Hierarchical motion understanding via motion programs. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 6568-6576).'
    bib = '''@inproceedings{kulal2021hierarchical,
  title={Hierarchical motion understanding via motion programs},
  author={Kulal, Sumith and Mao, Jiayuan and Aiken, Alex and Wu, Jiajun},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={6568--6576},
  year={2021}
}'''
    abstract = '''Current approaches to video analysis of human motion focus on raw pixels or keypoints as the basic units of reasoning. We posit that adding higher-level motion primitives, which can capture natural coarser units of motion such as backswing or follow-through, can be used to improve downstream analysis tasks. This higher level of abstraction can also capture key features, such as loops of repeated primitives, that are currently inaccessible at lower levels of representation. We therefore introduce Motion Programs, a neuro-symbolic, program-like representation that expresses motions as a composition of high-level primitives. We also present a system for automatically inducing motion programs from videos of human motion and for leveraging motion programs in video synthesis. Experiments show that motion programs can accurately describe a diverse set of human motions and the inferred programs contain semantically meaningful motion primitives, such as arm swings and jumping jacks. Our representation also benefits downstream tasks such as video interpolation and video prediction and outperforms off-the-shelf models. We further demonstrate how these programs can detect diverse kinds of repetitive motion and facilitate interactive video editing.'''
    tags = [computer_vision]
    my_notes = '''
Just one level of time hierarchy. Simple inductive bias to understand human videos. Ablation tests are a little insufficient, I would say. 
'''

class overcoming_the_disentanglement_vs_reconstruction_trade_off_via_jacobian_supervision:
    apa = 'Lezama, J. (2018, September). Overcoming the disentanglement vs reconstruction trade-off via Jacobian supervision. In International Conference on Learning Representations.'
    bib = '''@inproceedings{lezama2018overcoming,
  title={Overcoming the disentanglement vs reconstruction trade-off via Jacobian supervision},
  author={Lezama, Jos{\'e}},
  booktitle={International Conference on Learning Representations},
  year={2018}
}'''
    abstract = '''A major challenge in learning image representations is the disentangling of the factors of variation underlying the image formation.  This is typically achieved with an autoencoder architecture where a subset of the latent variables is constrained to correspond to specific factors, and the rest of them are considered nuisance variables. This approach has an important drawback: as the dimension of the nuisance variables is increased, image reconstruction is improved, but the decoder has the flexibility to ignore the specified factors, thus losing the ability to condition the output on them.  In this work, we propose to overcome this trade-off by progressively growing the dimension of the latent code, while constraining the Jacobian of the output image with respect to the disentangled variables to remain the same.  As a result, the obtained models are effective at both disentangling and reconstruction.  We demonstrate the applicability of this method in both unsupervised and supervised scenarios for learning disentangled representations. In a facial attribute manipulation task, we obtain high quality image generation while smoothly controlling dozens of attributes with a single model. This is an order of magnitude more disentangled factors than state-of-the-art methods, while obtaining visually similar or superior results, and avoiding adversarial training.'''

class time_in_distributed_real_time_systems:
    apa = 'Brandt, E., & Dannenberg, R. B. (1999). Time in distributed real-time systems.'
    bib = '''@article{brandt1999time,
  title={Time in distributed real-time systems},
  author={Brandt, Eli and Dannenberg, Roger B},
  year={1999},
  publisher={Carnegie Mellon University}
}'''
    abstract = '''A real-time music system is responsible for deciding what happens when, when each task runs and each message takes effect. This question becomes acute when there are several classes of tasks running and intercommunicating: user interface, control processing, and audio, for example. We briefly examine and classify past approaches and their applicability to distributed systems, then propose and discuss an alternative. The shared access to a sample clock that it requires is not trivial to achieve in a distributed system, so we describe and assess a way to do so.'''
    tags = [realtime]
    my_notes = '''
For ardu and proc, use midpoint estimate.  
'''

class make_a_video_text_to_video_generation_without_text_video_data:
    apa = 'Singer, U., Polyak, A., Hayes, T., Yin, X., An, J., Zhang, S., ... & Taigman, Y. (2022). Make-A-Video: Text-to-Video Generation without Text-Video Data. arXiv preprint arXiv:2209.14792.'
    bib = '''@article{singer2022make,
  title={Make-A-Video: Text-to-Video Generation without Text-Video Data},
  author={Singer, Uriel and Polyak, Adam and Hayes, Thomas and Yin, Xi and An, Jie and Zhang, Songyang and Hu, Qiyuan and Yang, Harry and Ashual, Oron and Gafni, Oran and others},
  journal={arXiv preprint arXiv:2209.14792},
  year={2022}
}'''
    abstract = '''We propose Make-A-Video -- an approach for directly translating the tremendous recent progress in Text-to-Image (T2I) generation to Text-to-Video (T2V). Our intuition is simple: learn what the world looks like and how it is described from paired text-image data, and learn how the world moves from unsupervised video footage. Make-A-Video has three advantages: (1) it accelerates training of the T2V model (it does not need to learn visual and multimodal representations from scratch), (2) it does not require paired text-video data, and (3) the generated videos inherit the vastness (diversity in aesthetic, fantastical depictions, etc.) of today's image generation models. We design a simple yet effective way to build on T2I models with novel and effective spatial-temporal modules. First, we decompose the full temporal U-Net and attention tensors and approximate them in space and time. Second, we design a spatial temporal pipeline to generate high resolution and frame rate videos with a video decoder, interpolation model and two super resolution models that can enable various applications besides T2V. In all aspects, spatial and temporal resolution, faithfulness to text, and quality, Make-A-Video sets the new state-of-the-art in text-to-video generation, as determined by both qualitative and quantitative measures.'''
    tags = [diffusion]
    my_notes = '''
It's text to image (embedding) to video.  
The image 2 video part finetunes an existing image diffusion model.  i.e. the 3rd D is added and then trained.  
Various details and techniques are worth learning from.  
'''

class learning_temporally_causal_latent_processes_from_general_temporal_data:
    apa = 'Yao, W., Sun, Y., Ho, A., Sun, C., & Zhang, K. (2021). Learning Temporally Causal Latent Processes from General Temporal Data. arXiv preprint arXiv:2110.05428.'
    bib = '''@article{yao2021learning,
  title={Learning Temporally Causal Latent Processes from General Temporal Data},
  author={Yao, Weiran and Sun, Yuewen and Ho, Alex and Sun, Changyin and Zhang, Kun},
  journal={arXiv preprint arXiv:2110.05428},
  year={2021}
}'''
    abstract = '''Our goal is to recover time-delayed latent causal variables and identify their relations from measured temporal data. Estimating causally-related latent variables from observations is particularly challenging as the latent variables are not uniquely recoverable in the most general case. In this work, we consider both a nonparametric, nonstationary setting and a parametric setting for the latent processes and propose two provable conditions under which temporally causal latent processes can be identified from their nonlinear mixtures. We propose LEAP, a theoretically-grounded framework that extends Variational AutoEncoders (VAEs) by enforcing our conditions through proper constraints in causal process prior. Experimental results on various datasets demonstrate that temporally causal latent processes are reliably identified from observed variables under different dependency structures and that our approach considerably outperforms baselines that do not properly leverage history or nonstationarity information. This demonstrates that using temporal information to learn latent processes from their invertible nonlinear mixtures in an unsupervised manner, for which we believe our work is one of the first, seems promising even without sparsity or minimality assumptions.'''
    tags = [causality, self_supervise, relation]
    my_notes = '''
"LEAP", "五小球".  
Using causality (高深，我不懂) to learn a system concepts from video.  
What I don't understand:  
why is it possible to infer causality when there's noise?  
Say x, \epsilon -> y. We observe x and y. How do we know the direction of the causation?  
'''

class the_surprising_effectiveness_of_equivariant_models_in_domains_with_latent_symmetry:
    ANONYMOUS = True
    assert not ANONYMOUS
    abstract = '''Extensive work has demonstrated that equivariant neural networks can significantly improve sample efficiency and generalization by enforcing an inductive bias in the network architecture. These applications typically assume that the domain symmetry is fully described by explicit transformations of the model inputs and outputs. However, many real-life applications contain only latent or partial symmetries which cannot be easily described by simple transformations of the input. In these cases, it is necessary to learn symmetry in the environment instead of imposing it mathematically on the network architecture. We discover, surprisingly, that imposing equivariance constraints that do not exactly match the domain symmetry is very helpful in learning the true symmetry in the environment. We differentiate between extrinsic and incorrect symmetry constraints and show that while imposing incorrect symmetry can impede the model's performance, imposing extrinsic symmetry can actually improve performance. We demonstrate that an equivariant model can significantly outperform non-equivariant methods on domains with latent symmetries both in supervised learning and in reinforcement learning for robotic manipulation and control problems.'''
    tags = [symmetry]
    my_notes = '''
it seems that plain encoders with wrong symm can learn well.  
'''

class diffusion_lm_improves_controllable_text_generation:
    apa = 'Li, X. L., Thickstun, J., Gulrajani, I., Liang, P., & Hashimoto, T. B. (2022). Diffusion-LM Improves Controllable Text Generation. arXiv preprint arXiv:2205.14217.'
    bib = '''@article{li2022diffusion,
  title={Diffusion-LM Improves Controllable Text Generation},
  author={Li, Xiang Lisa and Thickstun, John and Gulrajani, Ishaan and Liang, Percy and Hashimoto, Tatsunori B},
  journal={arXiv preprint arXiv:2205.14217},
  year={2022}
}'''
    abstract = '''Controlling the behavior of language models (LMs) without re-training is a major open problem in natural language generation. While recent works have demonstrated successes on controlling simple sentence attributes (e.g., sentiment), there has been little progress on complex, fine-grained controls (e.g., syntactic structure). To address this challenge, we develop a new non-autoregressive language model based on continuous diffusions that we call Diffusion-LM. Building upon the recent successes of diffusion models in continuous domains, Diffusion-LM iteratively denoises a sequence of Gaussian vectors into word vectors, yielding a sequence of intermediate latent variables. The continuous, hierarchical nature of these intermediate variables enables a simple gradient-based algorithm to perform complex, controllable generation tasks. We demonstrate successful control of Diffusion-LM for six challenging fine-grained control tasks, significantly outperforming prior work.'''
    tags = [diffusion, control, nlp]
    my_notes = '''
read abstract and Fig. 1.  
Fairly straight forward.  
Presented on study group: https://docs.google.com/presentation/d/1cuB6Y67DCRje5U3fvr08c2671iqo_4CG/edit?usp=share_link&ouid=111628173406875267677&rtpof=true&sd=true  

The condition is applied via classifier guidance.  
The classifier is trained to classify diffusion-intermediate vectors.  
During inference, alternate between classifier grad step and diffusion denoise step.  
'''

class exploiting_pre_trained_feature_networks_for_generative_adversarial_networks_in_audio_domain_loop_generation:
    apa = 'Yeh, Y. T., Chen, B. Y., & Yang, Y. H. (2022). Exploiting Pre-trained Feature Networks for Generative Adversarial Networks in Audio-domain Loop Generation. arXiv preprint arXiv:2209.01751.'
    bib = '''@article{yeh2022exploiting,
  title={Exploiting Pre-trained Feature Networks for Generative Adversarial Networks in Audio-domain Loop Generation},
  author={Yeh, Yen-Tung and Chen, Bo-Yu and Yang, Yi-Hsuan},
  journal={arXiv preprint arXiv:2209.01751},
  year={2022}
}'''
    abstract = '''While generative adversarial networks (GANs) have been widely used in research on audio generation, the training of a GAN model is known to be unstable, time consuming, and data inefficient. Among the attempts to ameliorate the training process of GANs, the idea of Projected GAN emerges as an effective solution for GAN-based image generation, establishing the state-of-the-art in different image applications. The core idea is to use a pre-trained classifier to constrain the feature space of the discriminator to stabilize and improve GAN training. This paper investigates whether Projected GAN can similarly improve audio generation, by evaluating the performance of a StyleGAN2-based audio-domain loop generation model with and without using a pre-trained feature space in the discriminator. Moreover, we compare the performance of using a general versus domain-specific classifier as the pre-trained audio classifier. With experiments on both drum loop and synth loop generation, we show that a general audio classifier works better, and that with Projected GAN our loop generation models can converge around 5 times faster without performance degradation.'''
    tags = [ismir2022, gan]

class projected_gans_converge_faster:
    apa = 'Sauer, A., Chitta, K., Müller, J., & Geiger, A. (2021). Projected gans converge faster. Advances in Neural Information Processing Systems, 34, 17480-17492.'
    bib = '''@article{sauer2021projected,
  title={Projected gans converge faster},
  author={Sauer, Axel and Chitta, Kashyap and M{\"u}ller, Jens and Geiger, Andreas},
  journal={Advances in Neural Information Processing Systems},
  volume={34},
  pages={17480--17492},
  year={2021}
}'''
    abstract = '''Generative Adversarial Networks (GANs) produce high-quality images but are challenging to train. They need careful regularization, vast amounts of compute, and expensive hyper-parameter sweeps. We make significant headway on these issues by projecting generated and real samples into a fixed, pretrained feature space. Motivated by the finding that the discriminator cannot fully exploit features from deeper layers of the pretrained model, we propose a more effective strategy that mixes features across channels and resolutions. Our Projected GAN improves image quality, sample efficiency, and convergence speed. It is further compatible with resolutions of up to one Megapixel and advances the state-of-the-art Fréchet Inception Distance (FID) on twenty-two benchmark datasets. Importantly, Projected GANs match the previously lowest FIDs up to 40 times faster, cutting the wall-clock time from 5 days to less than 3 hours given the same computational resources.'''
    tags = [gan]
    my_notes = '''
Uses random CCM and CSM to make discriminator look at the entire feature.  
Q1. Why is 1x1 conv not trivially invertible?  
    I wrote an email to ask the 1st author.  
Q2. Why does this method not suffer from vanishing gradients?  
'''

class equivariant_self_supervision_for_musical_tempo_estimation:
    apa = 'Quinton, E. (2022). Equivariant Self-Supervision for Musical Tempo Estimation. arXiv preprint arXiv:2209.01478.'
    bib = '''@article{quinton2022equivariant,
  title={Equivariant Self-Supervision for Musical Tempo Estimation},
  author={Quinton, Elio},
  journal={arXiv preprint arXiv:2209.01478},
  year={2022}
}'''
    abstract = '''Self-supervised methods have emerged as a promising avenue for representation learning in the recent years since they alleviate the need for labeled datasets, which are scarce and expensive to acquire. Contrastive methods are a popular choice for self-supervision in the audio domain, and typically provide a learning signal by forcing the model to be invariant to some transformations of the input. These methods, however, require measures such as negative sampling or some form of regularisation to be taken to prevent the model from collapsing on trivial solutions. In this work, instead of invariance, we propose to use equivariance as a self-supervision signal to learn audio tempo representations from unlabelled data. We derive a simple loss function that prevents the network from collapsing on a trivial solution during training, without requiring any form of regularisation or negative sampling. Our experiments show that it is possible to learn meaningful representations for tempo estimation by solely relying on equivariant self-supervision, achieving performance comparable with supervised methods on several benchmarks. As an added benefit, our method only requires moderate compute resources and therefore remains accessible to a wide research community.'''
    tags = [ismir2022, self_supervise]
    my_notes = '''
SPICE, but extracts tempo.  
(Not exactly, because SPICE is still different.)  
'''

class semantic_control_of_generative_musical_attributes:
    apa = None
    bib = None  # ismir2022
    abstract = '''Deep generative neural networks have been successful in tasks such as composing novel music and rendering expressive performance. Controllability is essential for building creative tools from such models. Recent work in this area has focused on disentangled latent space representations, but this is only part of the solution. Efficient control of semantic attributes must handle non-linearities and holes that occur in latent spaces, whilst minimising unwanted changes to other attributes. This paper introduces SeNT-Gen, a neural traversal algorithm that uses a secondary neural network to model the complex relationships between latent codes and musical attributes. This enables precise editing of semantic attributes that adapts to context. We demonstrate the method using the dMelodies dataset, and show strong performance for several VAE models.'''
    authors = '''Greenhill, Stewart*, Abdolshah, Majid, Le, Vuong, Gupta, Sunil, Venkatesh, Svetha'''
    tags = [ismir2022, control]
    my_notes = '''
if irrelevant dims should stay constant, why not prescribe?
limitations: all factors in the data are known, i.e., $c$ fully characterizes data.  
    when you require "change this and leave the rest unchanged", you have full knowledge of what "the rest" are. 
    rho: is it even right?
        if two factors are correlated, you can still disentangle. rho allows correlated dimensions to change. 
        the baseline would be `rho=1` always. Consider dimensions where z** != z*. z** is the "actually correct" z*. 
        given such a toy dataset, the only role of rho is to "clip" dimensions that are off because of data availablity. 
'''

class haptic_guidance_benefits_musical_motor_learning:
    apa = 'Grindlay, G. (2008, March). Haptic guidance benefits musical motor learning. In 2008 Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems (pp. 397-404). IEEE.'
    bib = None  # google freaked out
    abstract = '''This paper presents the results of a pilot experiment looking at the effect of haptic guidance on musical training. A percussion performance task was used where subjects learned to play short rhythmic sequences on a device capable of recording drumstick movements with a high degree of spatiotemporal accuracy. Subjects learned to perform the sequences under three primary training paradigms: listening to the rhythm (audio), being guided through the motions involved in the rhythm's performance (haptic), and being guided through the required motions while listening to the resulting sound (audio+haptic). Performance was assessed in terms of both timing and loudness (velocity) accuracy using several different metrics. Results indicate that haptic guidance can significantly benefit recall of both note timing and velocity. When subject performance was compared in terms of note velocity recall, the addition of haptic guidance to audio-based training produced a 17% reduction in final error when compared to audio training alone. When performance was evaluated in terms of liming recall, the combination of audio and haptic guidance led to an 18% reduction in early-stage error.'''
    tags = [haptic]
    my_notes = '''
cited in nime22 "A Computer-aided Multimodal Music Learning System with Curriculum: A Pilot Study"
Check "related works" section for a summary. 
'''

class haptic_technology_in_digital_music_learning_context_a_state_of_the_art_analysis:
    apa = 'Dörr, B., Norouzinia, F., Altmeyer, K., & Werth, D. (2022, October). Haptic Technology in Digital Music Learning Context: A State-of-the-Art Analysis. In European Conference on e-Learning (Vol. 21, No. 1, pp. 87-94). Academic Conferences International Limited.'
    bib = None  # google freaked out
    abstract = '''Digital media have become increasingly established in learning contexts in recent decades, and it seems impossibleto imagine education without them, especially in recent years. Various technological advances can be observed, such asdevelopments in virtual reality and augmented reality. To give learners a realistic impression of the virtual world, as manysensory impressions as possible should be addressed. However, current developments have mainly addressed the visual andauditory modalities, which make up two of the five human senses. Research and developments for the use of the othersenses are being made but at this stage they are not yet ready for mass use. Especially the sense of touch based on skin asthe largest human sensory organ or tactile and haptic perception seem to be of interest. Particularly in manual or medicalareas where motor skills are required, haptic technologies are declared to be supportive and beneficial. One area that hashardly focused on digital learning so far is the music sector. Learning a musical instrument in this context seems to be aninteresting field of research, as it not only promotes motor skills, but also cognitive development in both children and adults.To give an update on the technical developments in the field of digital teaching and learning in music, and especially tohighlight the use of haptic technologies, we will briefly review the state of the art in this paper. It begins with a brief overviewof the basics of digital learning and haptics, as well as previous work in this field. Using the method of a scoping review, thetopic of haptic technologies in the field of music education will be researched, analysed, and summarised according todefined criteria to give a condensed overview of it. The selected database and appropriate search strings will be used toachieve the aim of the paper. The results help to shed light on current research gaps and give indications for futuredevelopments of haptic technology in the music learning context.'''

class unsupervised_latent_tree_induction_with_deep_inside_outside_recursive_autoencoders:
    apa = 'Drozdov, A., Verga, P., Yadav, M., Iyyer, M., & McCallum, A. (2019). Unsupervised latent tree induction with deep inside-outside recursive autoencoders. arXiv preprint arXiv:1904.02142.'
    bib = '''@article{drozdov2019unsupervised,
  title={Unsupervised latent tree induction with deep inside-outside recursive autoencoders},
  author={Drozdov, Andrew and Verga, Pat and Yadav, Mohit and Iyyer, Mohit and McCallum, Andrew},
  journal={arXiv preprint arXiv:1904.02142},
  year={2019}
}'''
    abstract = '''We introduce deep inside-outside recursive autoencoders (DIORA), a fully-unsupervised method for discovering syntax that simultaneously learns representations for constituents within the induced tree. Our approach predicts each word in an input sentence conditioned on the rest of the sentence and uses inside-outside dynamic programming to consider all possible binary trees over the sentence. At test time the CKY algorithm extracts the highest scoring parse. DIORA achieves a new state-of-the-art F1 in unsupervised binary constituency parsing (unlabeled) in two benchmark datasets, WSJ and MultiNLI.'''
    tags = [self_supervise, repr_learning]

class vicreg_variance_invariance_covariance_regularization_for_self_supervised_learning:
    apa = 'Bardes, A., Ponce, J., & LeCun, Y. (2021). Vicreg: Variance-invariance-covariance regularization for self-supervised learning. arXiv preprint arXiv:2105.04906.'
    bib = '''@article{bardes2021vicreg,
  title={Vicreg: Variance-invariance-covariance regularization for self-supervised learning},
  author={Bardes, Adrien and Ponce, Jean and LeCun, Yann},
  journal={arXiv preprint arXiv:2105.04906},
  year={2021}
}'''
    abstract = '''Recent self-supervised methods for image representation learning are based on maximizing the agreement between embedding vectors from different views of the same image. A trivial solution is obtained when the encoder outputs constant vectors. This collapse problem is often avoided through implicit biases in the learning architecture, that often lack a clear justification or interpretation. In this paper, we introduce VICReg (Variance-Invariance-Covariance Regularization), a method that explicitly avoids the collapse problem with a simple regularization term on the variance of the embeddings along each dimension individually. VICReg combines the variance term with a decorrelation mechanism based on redundancy reduction and covariance regularization, and achieves results on par with the state of the art on several downstream tasks. In addition, we show that incorporating our new variance term into other methods helps stabilize the training and leads to performance improvements.'''
    tags = [self_supervise, jepa_or_jem]
    my_notes = '''
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
'''

class barlow_twins_self_supervised_learning_via_redundancy_reduction:
    apa = 'Zbontar, J., Jing, L., Misra, I., LeCun, Y., & Deny, S. (2021, July). Barlow twins: Self-supervised learning via redundancy reduction. In International Conference on Machine Learning (pp. 12310-12320). PMLR.'
    bib = '''@inproceedings{zbontar2021barlow,
  title={Barlow twins: Self-supervised learning via redundancy reduction},
  author={Zbontar, Jure and Jing, Li and Misra, Ishan and LeCun, Yann and Deny, St{\'e}phane},
  booktitle={International Conference on Machine Learning},
  pages={12310--12320},
  year={2021},
  organization={PMLR}
}'''
    abstract = '''Self-supervised learning (SSL) is rapidly closing the gap with supervised methods on large computer vision benchmarks. A successful approach to SSL is to learn embeddings which are invariant to distortions of the input sample. However, a recurring issue with this approach is the existence of trivial constant solutions. Most current methods avoid such solutions by careful implementation details. We propose an objective function that naturally avoids collapse by measuring the cross-correlation matrix between the outputs of two identical networks fed with distorted versions of a sample, and making it as close to the identity matrix as possible. This causes the embedding vectors of distorted versions of a sample to be similar, while minimizing the redundancy between the components of these vectors. The method is called Barlow Twins, owing to neuroscientist H. Barlow’s redundancy-reduction principle applied to a pair of identical networks. Barlow Twins does not require large batches nor asymmetry between the network twins such as a predictor network, gradient stopping, or a moving average on the weight updates. Intriguingly it benefits from very high-dimensional output vectors. Barlow Twins outperforms previous methods on ImageNet for semi-supervised classification in the low-data regime, and is on par with current state of the art for ImageNet classification with a linear classifier head, and for transfer tasks of classification and object detection.'''
    tags = [self_supervise, jepa_or_jem]
    my_notes = '''
Diff w/ VICReg: *Cross*-correlation between Z_A and Z_B.  
'''

class a_simple_framework_for_contrastive_learning_of_visual_representations:
    short = 'SimCLR'
    apa = 'Chen, T., Kornblith, S., Norouzi, M., & Hinton, G. (2020, November). A simple framework for contrastive learning of visual representations. In International conference on machine learning (pp. 1597-1607). PMLR.'
    bib = '''@inproceedings{chen2020simple,
  title={A simple framework for contrastive learning of visual representations},
  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
  booktitle={International conference on machine learning},
  pages={1597--1607},
  year={2020},
  organization={PMLR}
}'''
    abstract = '''This paper presents SimCLR: a simple framework for contrastive learning of visual representations. We simplify recently proposed contrastive self-supervised learning algorithms without requiring specialized architectures or a memory bank. In order to understand what enables the contrastive prediction tasks to learn useful representations, we systematically study the major components of our framework. We show that (1) composition of data augmentations plays a critical role in defining effective predictive tasks, (2) introducing a learnable nonlinear transformation between the representation and the contrastive loss substantially improves the quality of the learned representations, and (3) contrastive learning benefits from larger batch sizes and more training steps compared to supervised learning. By combining these findings, we are able to considerably outperform previous methods for self-supervised and semi-supervised learning on ImageNet. A linear classifier trained on self-supervised representations learned by SimCLR achieves 76.5% top-1 accuracy, which is a 7% relative improvement over previous state-of-the-art, matching the performance of a supervised ResNet-50. When fine-tuned on only 1% of the labels, we achieve 85.8% top-5 accuracy, outperforming AlexNet with 100X fewer labels.'''
    tags = [self_supervise, jepa_or_jem, contrastive]
    my_notes = '''
Diff w/ VICReg: 
    need to compute the denominator (negative pairs) for every datapoint within a batch. 
    VICReg only compute VIC once per batch. 
'''

class momentum_contrast_for_unsupervised_visual_representation_learning:
    short = 'MoCo'
    apa = 'He, K., Fan, H., Wu, Y., Xie, S., & Girshick, R. (2020). Momentum contrast for unsupervised visual representation learning. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (pp. 9729-9738).'
    bib = '''@inproceedings{he2020momentum,
  title={Momentum contrast for unsupervised visual representation learning},
  author={He, Kaiming and Fan, Haoqi and Wu, Yuxin and Xie, Saining and Girshick, Ross},
  booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
  pages={9729--9738},
  year={2020}
}'''
    abstract = '''We present Momentum Contrast (MoCo) for unsupervised visual representation learning. From a perspective on contrastive learning as dictionary look-up, we build a dynamic dictionary with a queue and a moving-averaged encoder. This enables building a large and consistent dictionary on-the-fly that facilitates contrastive unsupervised learning. MoCo provides competitive results under the common linear protocol on ImageNet classification. More importantly, the representations learned by MoCo transfer well to downstream tasks. MoCo can outperform its supervised pre-training counterpart in 7 detection/segmentation tasks on PASCAL VOC, COCO, and other datasets, sometimes surpassing it by large margins. This suggests that the gap between unsupervised and supervised representation learning has been largely closed in many vision tasks.'''
    tags = [self_supervise, jepa_or_jem, contrastive]

class representation_learning_with_contrastive_predictive_coding:
    short = 'infoNCE', 'CPC'
    apa = 'Oord, A. V. D., Li, Y., & Vinyals, O. (2018). Representation learning with contrastive predictive coding. arXiv preprint arXiv:1807.03748.'
    bib = '''@article{oord2018representation,
  title={Representation learning with contrastive predictive coding},
  author={Oord, Aaron van den and Li, Yazhe and Vinyals, Oriol},
  journal={arXiv preprint arXiv:1807.03748},
  year={2018}
}'''
    abstract = '''While supervised learning has enabled great progress in many applications, unsupervised learning has not seen such widespread adoption, and remains an important and challenging endeavor for artificial intelligence. In this work, we propose a universal unsupervised learning approach to extract useful representations from high-dimensional data, which we call Contrastive Predictive Coding. The key insight of our model is to learn such representations by predicting the future in latent space by using powerful autoregressive models. We use a probabilistic contrastive loss which induces the latent space to capture information that is maximally useful to predict future samples. It also makes the model tractable by using negative sampling. While most prior work has focused on evaluating representations for a particular modality, we demonstrate that our approach is able to learn useful representations achieving strong performance on four distinct domains: speech, images, text and reinforcement learning in 3D environments.'''
    tags = [self_supervise, jepa_or_jem, contrastive]

class whitening_for_self_supervised_representation_learning:
    apa = 'Ermolov, A., Siarohin, A., Sangineto, E., & Sebe, N. (2021, July). Whitening for self-supervised representation learning. In International Conference on Machine Learning (pp. 3015-3024). PMLR.'
    bib = '''@inproceedings{ermolov2021whitening,
  title={Whitening for self-supervised representation learning},
  author={Ermolov, Aleksandr and Siarohin, Aliaksandr and Sangineto, Enver and Sebe, Nicu},
  booktitle={International Conference on Machine Learning},
  pages={3015--3024},
  year={2021},
  organization={PMLR}
}'''
    abstract = '''Most of the current self-supervised representation learning (SSL) methods are based on the contrastive loss and the instance-discrimination task, where augmented versions of the same image instance ("positives") are contrasted with instances extracted from other images ("negatives"). For the learning to be effective, many negatives should be compared with a positive pair, which is computationally demanding. In this paper, we propose a different direction and a new loss function for SSL, which is based on the whitening of the latent-space features. The whitening operation has a "scattering" effect on the batch samples, avoiding degenerate solutions where all the sample representations collapse to a single point. Our solution does not require asymmetric networks and it is conceptually simple. Moreover, since negatives are not needed, we can extract multiple positive pairs from the same image instance. The source code of the method and of all the experiments is available at: https://github.com/htdt/self-supervised.'''
    tags = [self_supervise, jepa_or_jem]

class bootstrap_your_own_latent_a_new_approach_to_self_supervised_learning:
    apa = 'Grill, J. B., Strub, F., Altché, F., Tallec, C., Richemond, P., Buchatskaya, E., ... & Valko, M. (2020). Bootstrap your own latent-a new approach to self-supervised learning. Advances in neural information processing systems, 33, 21271-21284.'
    bib = '''@article{grill2020bootstrap,
  title={Bootstrap your own latent-a new approach to self-supervised learning},
  author={Grill, Jean-Bastien and Strub, Florian and Altch{\'e}, Florent and Tallec, Corentin and Richemond, Pierre and Buchatskaya, Elena and Doersch, Carl and Avila Pires, Bernardo and Guo, Zhaohan and Gheshlaghi Azar, Mohammad and others},
  journal={Advances in neural information processing systems},
  volume={33},
  pages={21271--21284},
  year={2020}
}'''
    abstract = '''We introduce Bootstrap Your Own Latent (BYOL), a new approach to self-supervised image representation learning. BYOL relies on two neural networks, referred to as online and target networks, that interact and learn from each other. From an augmented view of an image, we train the online network to predict the target network representation of the same image under a different augmented view. At the same time, we update the target network with a slow-moving average of the online network. While state-of-the art methods intrinsically rely on negative pairs, BYOL achieves a new state of the art without them. BYOL reaches 74.3% top-1 classification accuracy on ImageNet using the standard linear evaluation protocol with a standard ResNet-50 architecture and 79.6% with a larger ResNet. We also show that BYOL performs on par or better than the current state of the art on both transfer and semi-supervised benchmarks.'''
    tags = [self_supervise, jepa_or_jem]

class exploring_simple_siamese_representation_learning:
    short = 'SimSiam'
    apa = 'Chen, X., & He, K. (2021). Exploring simple siamese representation learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 15750-15758).'
    bib = '''@inproceedings{chen2021exploring,
  title={Exploring simple siamese representation learning},
  author={Chen, Xinlei and He, Kaiming},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={15750--15758},
  year={2021}
}'''
    abstract = '''Siamese networks have become a common structure in various recent models for unsupervised visual representation learning. These models maximize the similarity between two augmentations of one image, subject to certain conditions for avoiding collapsing solutions. In this paper, we report surprising empirical results that simple Siamese networks can learn meaningful representations even using none of the following: (i) negative sample pairs, (ii) large batches, (iii) momentum encoders. Our experiments show that collapsing solutions do exist for the loss and structure, but a stop-gradient operation plays an essential role in preventing collapsing. We provide a hypothesis on the implication of stop-gradient, and further show proof-of-concept experiments verifying it. Our "SimSiam" method achieves competitive results on ImageNet and downstream tasks. We hope this simple baseline will motivate people to rethink the roles of Siamese architectures for unsupervised representation learning. Code is made available. (https://github.com/facebookresearch/simsiam)'''
    tags = [self_supervise, jepa_or_jem]

class unsupervised_learning_of_visual_features_by_contrasting_cluster_assignments:
    short = 'SwAV'
    apa = 'Caron, M., Misra, I., Mairal, J., Goyal, P., Bojanowski, P., & Joulin, A. (2020). Unsupervised learning of visual features by contrasting cluster assignments. Advances in Neural Information Processing Systems, 33, 9912-9924.'
    bib = '''@article{caron2020unsupervised,
  title={Unsupervised learning of visual features by contrasting cluster assignments},
  author={Caron, Mathilde and Misra, Ishan and Mairal, Julien and Goyal, Priya and Bojanowski, Piotr and Joulin, Armand},
  journal={Advances in Neural Information Processing Systems},
  volume={33},
  pages={9912--9924},
  year={2020}
}'''
    abstract = '''Unsupervised image representations have significantly reduced the gap with supervised pretraining, notably with the recent achievements of contrastive learning methods. These contrastive methods typically work online and rely on a large number of explicit pairwise feature comparisons, which is computationally challenging. In this paper, we propose an online algorithm, SwAV, that takes advantage of contrastive methods without requiring to compute pairwise comparisons. Specifically, our method simultaneously clusters the data while enforcing consistency between cluster assignments produced for different augmentations (or views) of the same image, instead of comparing features directly as in contrastive learning. Simply put, we use a swapped prediction mechanism where we predict the code of a view from the representation of another view. Our method can be trained with large and small batches and can scale to unlimited amounts of data. Compared to previous contrastive methods, our method is more memory efficient since it does not require a large memory bank or a special momentum network. In addition, we also propose a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. We validate our findings by achieving 75.3% top-1 accuracy on ImageNet with ResNet-50, as well as surpassing supervised pretraining on all the considered transfer tasks.'''
    tags = [self_supervise, jepa_or_jem]
