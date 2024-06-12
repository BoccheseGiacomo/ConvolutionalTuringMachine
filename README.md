# Convolutional Turing Machine (CTM): studying Meta-Learning Emergence from Cellular Automata

## Introduction

The CTM is a research project designed to explore adaptive learning systems within computational models, drawing inspiration from the dynamic behaviors of Lenia-like cellular automata. Central to its design is the use of convolution operations in a two-dimensional geometric space, enhanced by Adaptive Computation Time (ACT) for introducing halting properties and flow control. This mechanism positions the CTM as a finite state approximation of a universal Turing machine.

What sets the CTM apart is its inherent structure that not only enables spontaneous meta-learning but also allows the emergence of self-reinforcement learning and dynamic memory organization.

The CTM can be envisioned as a form of artificial intelligence where every aspect is emergent, without relying on pre-defined assumptions. This approach mirrors the intricate, life-like behaviors found in nature, where complexity and adaptability arise from deeply non-linear, interactive systems that evolve and get selected in order to best match a dynamic global maximum.

It's important to emphasize that the CTM project, at this juncture, is highly experimental. *Some of the theoretical claims present in this description are not formally proved yet, many of them come from a kind of "rigorous deduction" and some intuition based on known concepts in deep learning and emergent systems*. The future steps outlined are exploratory in nature and aimed at gradually uncovering the potential and limitations of the model. As the project progresses, these steps will be critical in transitioning from heuristical concepts to tangible results and insights.



<div>
  <img src="https://github.com/BoccheseGiacomo/ConvolutionalTuringMachine/assets/104854120/e275428b-72fc-42b0-b4e3-4f2b67b5bd2d" alt="CTM Simulation" width="500" height="auto">
  <br>
  <p><em>Figure 1: A showing the inference process of a random, non trained, CTM.</em></p>
</div>


Convolutional Turing Machine © 2023 by Giacomo Bocchese is licensed under CC BY-NC-SA 4.0 
<br>Additional license requirement: anyone that uses this project for any reason, has to cite the project with the citation shown below.

## Project Vision and Objectives

CTM is envisioned as a cellular automaton with an inherent capacity for learning and adaptability. Its central goal is to demonstrate the emergence of desired behaviors and to model any algorithm or function of interest, provided enough 2-d space and computation time. The project is anchored in several key objectives:

- **Complex Behavior Simulation**: The kernel of the CTM is analogous to a stencil in finite difference simulations, capable of simulating intricate behaviors akin to those observed in nonlinear partial differential equations. This ability opens the door to modeling complex physical structures, potentially emulating the spatial configurations of neuronal networks or other ways of modeling an external world.

- **Halting and Flow control**: Incorporating Adaptive Computation Time (ACT) into the CTM is pivotal for expanding its computational repertoire, particularly in terms of representability. ACT introduces halting-based flow control that allows for looping operations, a crucial aspect for broadening the range of computable functions. This enhancement is not just about efficiency; it fundamentally transforms the CTM's capability to simulate more complex processes using less parameters (thus improving generalization). By enabling controlled looping and flow manipulation within its operations, the CTM dramatically extends its ability to represent a diverse array of functions through autoregressivity. Furthermore, this aspect of flow control is integral to the concept of Turing completeness. In a theoretical framework where the state space and computation time are unbounded, ACT positions the CTM to potentially touch on universality in computation. A note about the dimension of the kernel: in order to give this ability of turing completeness we need to understand what is the minimal kernel dimension and minimal encoded state dimension that allows for universality, even if we believe a small kernel like 3x3 or 5x5 is enough, since the computational process is encoded more on the initial state that on the kernel. The state space is not only important for "storing" information but is an active part in the role of computation. Furthermore, we still have to experiment if linear convolution is enough, because maybe also non-linear operations are to be added.
 
- **Meta-Learning**: CTM is designed not just to learn thanks to external optimizers but to autonomously develop internal reinforcement learning algorithms. These algorithms, activated by external rewards fed into the state space, are intended to surpass the efficiency of genetic algorithms during training.

- **Self-Reinforcement Learning**: The model is also hypothesized to engage in what we called "Self-Reinforcement Learning", evolving internal reward mechanisms that guide it toward optimal behaviors with maximal data efficiency and generalization. Notably, the CTM can engage in a form of 'cognitive simulation' or 'imagination dream', akin to human mental experimentation. In this state, devoid of external data, the model internally simulates scenarios, hypothesizing outcomes and thus self-generating synthetic data and rewards. This process allows the CTM to strategize and evolve toward optimal behaviors, mirroring the human ability to mentally forecast and strategize before actual implementation, and generalizing thanks to this self-generated data.


## Internal mechanics description

### Initial Setup and Configuration

The Convolutional Turing Machine (CTM) operates within a predefined two-dimensional grid, each cell of which can hold a numerical value representing its current state.

Key components within this grid are designated for specific roles:
- **Input Cells**: Located at predetermined positions, these cells are where external data inputs are received.
- **Output Cells**: These cells are monitored to extract the CTM's output or response after processing.
- **Reward Cell**: Receives an external reward signal, crucial for the internal learning phase.
- **Halting Cell**: Determines when the CTM stops its computation for a given input, controlling the computation length.

### Kernel

At the heart of the CTM is the convolutional kernel, a small matrix that dictates the interaction between a cell and its neighbors during state evolution. This makes the model "fully local" meaning that its evolution depends on near cell interaction.

### Inference and Processing

During an inference cycle, the CTM undergoes the following steps:
1. **Receiving Inputs**: Data inputs are fed into the designated input cells.
2. **Convolutional Processing**: The grid undergoes state transitions driven by the convolution operation with the kernel, blending local cell values to evolve the grid's state.
3. **Halting Condition**: The process repeats until the state of the halting cell reaches a predefined threshold, signaling the end of computation.
4. **Output Retrieval**: The state values in the output cells are then interpreted as the CTM's processed result.
5. **Reward Integration (For Learning)**: In learning scenarios, an external reward is provided to the reward cell, influencing the latent state space's optimization but not altering the kernel.

## Mathematical description

### Definitions:

$$
\begin{align*}
&x \in \mathbb{R}^d \quad \text{(Input vector} \rightarrow \text{multi-index } x_{\text{idx}} \text{ for indexing the input cells in } s) \\
&y \in \mathbb{R}^q \quad \text{(Output vector} \rightarrow \text{multi-index } y_{\text{idx}} \text{ for indexing } y) \\
&r \in [-1,1] \quad \text{(Reward (scalar) } \rightarrow \text{single-index } r_{\text{idx}}) \\
&s \in \mathbb{R}^{n \times n} \quad \text{(State space)} \\
&k \in \mathbb{R}^{m \times m}, \quad m \ll n \\
\end{align*}
$$

### BC: Boundary Conditions:

$$
\begin{align*}
&s[x_{\text{idx}}] = x \\
&s[r_{\text{idx}}] = r
\end{align*}
$$

### Inference:

$$
\begin{align*}
&\text{- Load a pretrained } s(t=0) \text{ (initial state) and a pretrained kernel } k \\
&\text{- Take the input } x \text{ and the reward } r \text{ coming from the environment feedback of the previous step} \\
& \\
&\text{While } s_t[h_{\text{idx}}] < 1: \quad \text{(until halting)} \\
&\quad \text{Apply BC overwriting input and reward cells of } s_t \\
&\quad s_{t+1} = f(k * s_t) \quad \text{(Convolution + function, if nonlinear function or identity (in this implementation, identity function))} \\
&\\
&\text{When halts: } s_{\text{halt}} = s_t \\
&\quad y = s_{\text{halt}}[y_{\text{idx}}] \\
&\\
&\text{- End or continue to next input } x, \text{ keeping the last state } s_{\text{halt}} \text{ as the new initial state } s_{\text{new}}(t=0) \\
&\text{- If continuing, interact with the environment or dataset and get the new reward } r_{\text{new}} \text{ for the next prediction} 
\end{align*}
$$



## Challenges and Training

One of the most intriguing yet challenging aspects of the CTM is its training process. The project steps away from conventional optimization methods used in Artificial Neural Networks (ANNs), such as gradient descent, and instead embraces a more exploratory approach:

- **Genetic Algorithms for Exploration**: Training the CTM is envisioned to rely heavily on genetic algorithms. The focus is on exploration, encouraging a wide variety of policies and behaviors to be experimented with.
- **Complex Training Dynamics**: Given the theoretical capabilities of the CTM, training it to harness these abilities is an ambitious endeavor. The model needs to propagate information effectively, construct complex internal models, and potentially develop its reinforcement learning algorithms.
- **Alternatives**: We thought to use GAs because they are very versatile and does no prior assumption on processes and data, but valid candidates are other zeroth-order optimization algorithms like simulated annealing and particle swarm optimization, or some reinforcement learning method.


## Training Phase of the CTM with Genetic Algorithms

### Components and Initialization

In the training phase of the CTM, the primary components subject to training are:
- **Kernel Values**: These define the convolutional behavior of the model.
- **Initial State of the Grid**: This can include the entire grid or a subset, with some parts potentially fixed to a zero state.

The training process begins with the random initialization of these components across a population of `n` CTM models. Each model in the population is uniquely characterized by its own set of kernel values and initial state.

### Simulation and Selection

1. **Running Simulations**: For each model in the population, a simulation is run where the model processes given inputs and generates outputs. During this phase, a reward is also provided, which is crucial for guiding the learning process.

2. **Selection of the Best Models**: Post-simulation, models are evaluated based on their performance – how well they processed the inputs to match the expected outputs and utilized the reward. The best-performing models are selected for the next stage.

3. **Reproduction with Genetic Operators**: The selected models undergo reproduction, where genetic operations like mutation and crossover are applied. This step generates a new population of models, inheriting and variating traits from the successful models of the previous generation.

4. **Iterative Process**: This process of simulation, selection, and reproduction is repeated over multiple generations. With each iteration, the models are expected to progressively improve in their task performance.

### Emergence of Meta-Learning

The emergence of meta-learning within the CTM is anticipated due to the system's inherent flexibility and capacity to model a broad class of algorithms, including internal optimizers. Theoretically, if a model, by chance, develops an ability to internally update its state in response the external rewards, it would exhibit faster and more efficient learning compared to other models. Such a model would have a higher chance of being selected in the GA process, thereby propagating its traits to subsequent generations.

Over time, this leads to the dominance of models capable of such internal learning optimizations, making meta-learning an emergent standard within the population. This evolutionary process hinges on the principle that models which can internally incorporate reward information to refine their state will outperform and outlast those that do not, leading to the natural emergence of meta-learning capabilities in the CTM.

The same may happen for Self-Reinforcement Learning, it may emerge from chance and then get selected.


## Current State and Future Directions

### Current Progress

As of now, the CTM project is in its early developmental phase. The foundational model has been established, but it has yet to be applied or tested in practical scenarios. Key aspects like training methodologies and their effectiveness in achieving desired behaviors are still theoretical and await empirical validation. To date, no concrete results have been achieved; the project remains in the realm of setup and initial exploration.

### Future Steps

Looking ahead, the project has several critical milestones to achieve:

1. **Implementing a Genetic Algorithm**: The initial phase of training will involve the implementation of a genetic algorithm. This step is fundamental for basic training and setting the groundwork for more advanced learning processes.

2. **Task Learning Without Reward**: An early experiment will involve attempting to train the CTM to learn a specific task using the genetic algorithm alone, without any external reward mechanism. This test aims to explore the CTM's capabilities in a more constrained learning environment.

3. **Extensive Training with Rewards**: The subsequent phase will focus on extensively training the CTM across a variety of tasks while incorporating external rewards. The goal here is to observe and measure the emergence of meta-learning. This stage is crucial for understanding whether and how the CTM develops its internal learning strategies and adapts to diverse challenges.

4. **Experimenting with non-linearities**: Even if it may be not needed, it would be fundamental to experiment with adding non-linear transformations to the system for better integration with Lenia Cellular Automata, that uses both convolution and non-linear growth functions.
   
5. **Improvments: additional dimension**: To enhance the complexity of the behaviours we plan to transform the CTM to a 3-d system with dimension (n,n,2) instead of (n,n) by adding a new stacked layer below: long term memory layer: this layer controls the diffusivity of the system by a multiplicative factor for each cell, and is influenced from the activations of the upper layer. This way the system can spontaneously evolve "computing pathways". Even if this step may not increase the expressivity of the system, it's likely to increase the stability and the interpretability of the model. For even more complex configurations, we can add multiple stacked layers, with the general dimension (n,n,m). The interaction system can also include non-linearities.

## Installation and Usage
The actual setup is manual: you need to clone the repo and go with your python environment.

## Contributions and Collaboration

We welcome contributions and collaborations from researchers, enthusiasts, and anyone interested in exploring the frontiers of cellular automata and state space models. If you have ideas, suggestions, or want to contribute to the project, feel free to reach out or submit a pull request.
Any modification should be done accordingly to the license: CC BY-NC-SA 4.0. 
If using this for commercial purpose please contact me for obtaining a "special license" under private agreement.

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
