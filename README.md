# Convolutional Turing Machine (CTM): studying Meta-Learning Emergence from Cellular Automata

## Introduction

The CTM is a research project designed to explore adaptive learning systems within computational models, drawing inspiration from the dynamic behaviors of Lenia-like cellular automata. Central to its design is the use of convolution operations in a two-dimensional geometric space, enhanced by Adaptive Computation Time (ACT) for introducing halting properties and flow control. This mechanism positions the CTM as a finite state approximation of a universal Turing machine.

What sets the CTM apart is its inherent structure that not only enables spontaneous meta-learning but also allows the emergence of self-reinforcement learning and dynamic memory organization.

The CTM can be envisioned as a form of artificial intelligence where every aspect is emergent, without relying on pre-defined assumptions. This approach mirrors the intricate, life-like behaviors found in nature, where complexity and adaptability arise from deeply non-linear, interactive systems that evolve and get selected in order to best match a dynamic global maximum.

## Project Vision and Objectives

CTM is envisioned as a cellular automaton with an inherent capacity for learning and adaptability. Its central goal is to demonstrate the emergence of desired behaviors and to model any algorithm or function of interest, provided enough 2-d space and computation time. The project is anchored in several key objectives:

- **Complex Behavior Simulation**: The kernel of the CTM is analogous to a stencil in finite difference simulations, capable of simulating intricate behaviors akin to those observed in nonlinear partial differential equations. This ability opens the door to modeling complex physical structures, potentially emulating the spatial configurations of neuronal networks or other ways of modeling an external world.
 
- **Meta-Learning**: CTM is designed not just to learn thanks to external optimizers but to autonomously develop internal reinforcement learning algorithms. These algorithms, activated by external rewards fed into the state space, are intended to surpass the efficiency of genetic algorithms.

- **Self-Reinforcement Learning**: The model is also hypothesized to engage in what we called "Self-Reinforcement Learning", evolving internal reward mechanisms that guide it toward optimal behaviors with maximal data efficiency and generalization. Notably, the CTM can engage in a form of 'cognitive simulation' or 'imagination dream', akin to human mental experimentation. In this state, devoid of external data, the model internally simulates scenarios, hypothesizing outcomes and self-generating synthetic data and rewards. This process allows the CTM to strategize and evolve toward optimal behaviors, mirroring the human ability to mentally forecast and strategize before actual implementation.
  

## Challenges and Training

One of the most intriguing yet challenging aspects of the CTM is its training process. The project steps away from conventional optimization methods used in Artificial Neural Networks (ANNs), such as gradient descent, and instead embraces a more exploratory approach:

- **Genetic Algorithms for Exploration**: Training the CTM is envisioned to rely heavily on genetic algorithms. The focus is on exploration, encouraging a wide variety of policies and behaviors to be experimented with.
- **Complex Training Dynamics**: Given the theoretical capabilities of the CTM, training it to harness these abilities is an ambitious endeavor. The model needs to propagate information effectively, construct complex internal models, and potentially develop its reinforcement learning algorithms.

## Current State and Future Directions

The CTM project is in its nascent stages, with training methodologies and practical applications still under development. The current focus is on understanding the theoretical limits and practical capabilities of the model, particularly in training it to achieve the envisioned emergent behaviors.

Future steps:
-implementing a genetic algorithm for basic training
-try to make it learn a task with GA alone (without reward)
-running it a lot on different tasks with reward and measuring if meta learning actually emerges

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

