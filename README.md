# Convolutional Turing Machine (CTM): studying Meta-Learning Emergence from Cellular Automata

## Introduction

The CTM is a research project designed to explore adaptive learning systems within computational models, drawing inspiration from the dynamic behaviors of Lenia-like cellular automata. Central to its design is the use of convolution operations in a two-dimensional geometric space, enhanced by Adaptive Computation Time (ACT) for introducing halting properties and flow control. This mechanism positions the CTM as a finite state approximation of a universal Turing machine.

What sets the CTM apart is its inherent structure that not only enables spontaneous meta-learning but also allows the emergence of self-reinforcement learning and dynamic memory organization.

The CTM can be envisioned as a form of artificial intelligence where every aspect is emergent, without relying on pre-defined assumptions. This approach mirrors the intricate, life-like behaviors found in nature, where complexity and adaptability arise from deeply non-linear, interactive systems that evolve and get selected in order to best match a dynamic global maximum.

## Project Vision and Objectives

CTM is envisioned as a cellular automaton with an inherent capacity for learning and adaptability. Its central goal is to demonstrate the emergence of desired behaviors and to model any algorithm or function of interest, provided enough 2-d space and computation time. The project is anchored in several key objectives:

- **Complex Behavior Simulation**: The kernel of the CTM is analogous to a stencil in finite difference simulations, capable of simulating intricate behaviors akin to those observed in nonlinear partial differential equations. This ability opens the door to modeling complex physical structures, potentially emulating the spatial configurations of neuronal networks or other ways of modeling an external world.

- **Halting and Flow control**: Incorporating Adaptive Computation Time (ACT) into the CTM is pivotal for expanding its computational repertoire, particularly in terms of representability. ACT introduces halting-based flow control that allows for looping operations, a crucial aspect for broadening the range of computable functions. This enhancement is not just about efficiency; it fundamentally transforms the CTM's capability to simulate more complex processes. By enabling controlled looping and flow manipulation within its operations, the CTM dramatically extends its ability to represent a diverse array of functions through autoregressivity. Furthermore, this aspect of flow control is integral to the concept of Turing completeness. In a theoretical framework where the state space and computation time are unbounded, ACT positions the CTM to potentially touch on universality in computation. A note about the dimension of the kernel: in order to give this ability of turing completeness we need to understand what is the minimal kernel dimension and minimal encoded state dimension that allows for universality, even if we believe a small kernel like 3x3 or 5x5 is enough, since the computational process is encoded more on the initial state that on the kernel. The state space is not only important for "storing" information but is an active part in the role of computation.
 
- **Meta-Learning**: CTM is designed not just to learn thanks to external optimizers but to autonomously develop internal reinforcement learning algorithms. These algorithms, activated by external rewards fed into the state space, are intended to surpass the efficiency of genetic algorithms.

- **Self-Reinforcement Learning**: The model is also hypothesized to engage in what we called "Self-Reinforcement Learning", evolving internal reward mechanisms that guide it toward optimal behaviors with maximal data efficiency and generalization. Notably, the CTM can engage in a form of 'cognitive simulation' or 'imagination dream', akin to human mental experimentation. In this state, devoid of external data, the model internally simulates scenarios, hypothesizing outcomes and thus self-generating synthetic data and rewards. This process allows the CTM to strategize and evolve toward optimal behaviors, mirroring the human ability to mentally forecast and strategize before actual implementation, and generalizing thanks to this self-generated data.
  

## Challenges and Training

One of the most intriguing yet challenging aspects of the CTM is its training process. The project steps away from conventional optimization methods used in Artificial Neural Networks (ANNs), such as gradient descent, and instead embraces a more exploratory approach:

- **Genetic Algorithms for Exploration**: Training the CTM is envisioned to rely heavily on genetic algorithms. The focus is on exploration, encouraging a wide variety of policies and behaviors to be experimented with.
- **Complex Training Dynamics**: Given the theoretical capabilities of the CTM, training it to harness these abilities is an ambitious endeavor. The model needs to propagate information effectively, construct complex internal models, and potentially develop its reinforcement learning algorithms.
- **Alternatives**: We thought to use GAs because they are very versatile and does no prior assumption on processes and data, but valid candidates are other zeroth-order optimization algorithms like simulated annealing and particle swarm optimization, or some reinforcement learning method.


## Current State and Future Directions

### Current Progress

As of now, the CTM project is in its early developmental phase. The foundational model has been established, but it has yet to be applied or tested in practical scenarios. Key aspects like training methodologies and their effectiveness in achieving desired behaviors are still theoretical and await empirical validation. To date, no concrete results have been achieved; the project remains in the realm of setup and initial exploration.

### Future Steps

Looking ahead, the project has several critical milestones to achieve:

1. **Implementing a Genetic Algorithm**: The initial phase of training will involve the implementation of a genetic algorithm. This step is fundamental for basic training and setting the groundwork for more advanced learning processes.

2. **Task Learning Without Reward**: An early experiment will involve attempting to train the CTM to learn a specific task using the genetic algorithm alone, without any external reward mechanism. This test aims to explore the CTM's capabilities in a more constrained learning environment.

3. **Extensive Testing with Rewards**: The subsequent phase will focus on extensively running the CTM across a variety of tasks while incorporating external rewards. The goal here is to observe and measure the emergence of meta-learning. This stage is crucial for understanding whether and how the CTM develops its internal learning strategies and adapts to diverse challenges.

## Installation and Usage
The actual setup is manual: you need to clone the repo and go with your python environment.

## Contributions and Collaboration

We welcome contributions and collaborations from researchers, enthusiasts, and anyone interested in exploring the frontiers of cellular automata and state space models. If you have ideas, suggestions, or want to contribute to the project, feel free to reach out or submit a pull request.

## Citation

If you utilize the CTM in your research or projects, kindly cite this work as follows:

```bibtex
@misc{ctm2023,
  author = {Giacomo Bocchese},
  title = {Convolutional Turing Machine: studying Meta-Learning Emergence from Cellular Automata},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/BoccheseGiacomo/ConvolutionalTuringMachine}}
}
```

