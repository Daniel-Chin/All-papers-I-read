from .tags import *

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
    tags = [haptic, vibration, passive_learning]
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
    my_notes = 'Hardly a good paper.'
