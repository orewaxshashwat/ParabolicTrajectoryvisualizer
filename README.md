 **Parabolic Trajectory Visualizer**

A Python-based simulation project that visualizes the parabolic motion of a projectile using mathematical equations and interactive graphs.

This project demonstrates how different initial velocities and launch angles affect the trajectory of a projectile. It uses Python, NumPy, and Matplotlib to calculate and visualize projectile motion in real time.

** Project Overview**

Projectile motion is a type of two-dimensional motion in which an object moves under the influence of gravity after being launched at an angle.

This visualizer allows users to experiment with different initial velocities and launch angles and observe how they affect the projectile's path.

The project provides two interactive graphs:

Graph 1 – Effect of Velocity: Keeps the launch angle constant and changes the initial velocity to visualize different trajectories.
Graph 2 – Effect of Angle: Keeps the initial velocity constant and changes the launch angle to compare different trajectories.

It also calculates important projectile motion parameters and displays them in the terminal.

 Features
Interactive projectile trajectory visualization.
Analyze the effect of initial velocity on projectile motion.
Analyze the effect of launch angle on projectile motion.
Calculate time of flight.
Calculate maximum height.
Calculate horizontal range.
Real-time graph updates using Matplotlib.
Multiple trajectory comparisons on the same graph.
User-friendly terminal-based input system.
 Physics and Mathematical Equations

The simulation uses the standard equations of projectile motion, assuming:

Air resistance is neglected.
Gravitational acceleration is constant.
The projectile lands at the same height from which it was launched.

Let:

u = Initial velocity (m/s)
θ = Launch angle (degrees)
g = Acceleration due to gravity (9.8 m/s²)
T = Time of flight (seconds)
H = Maximum height (meters)
R = Horizontal range (meters)
1. Time of Flight

T = (2u sin θ) / g

2. Maximum Height

H = (u² sin² θ) / (2g)

3. Horizontal Range

R = (u² sin 2θ) / g

4. Horizontal Position

x = u cos θ × t

5. Vertical Position

y = u sin θ × t - (1/2)gt²

These equations are used to calculate the projectile's position at different time intervals and generate its parabolic trajectory.

 **Technologies Used**
Python – Main programming language.
NumPy – Mathematical calculations and numerical operations.
Matplotlib – Graph plotting and trajectory visualization.
 Project Structure
text
Parabolic-Trajectory-Visualizer/
│
├── main.py          # Main simulation source code
├── README.md        # Project documentation
└── requirements.txt # Project dependencies

 Installation and Setup

Follow these steps to run the project on your local machine.

Step 1: Clone the Repository
bash
git clone https://github.com/your-username/Parabolic-Trajectory-Visualizer.git

Step 2: Navigate to the Project Directory
bash
cd Parabolic-Trajectory-Visualizer

Step 3: Install Dependencies
bash
pip install -r requirements.txt


Alternatively, install the libraries individually:

bash
pip install numpy matplotlib

Step 4: Run the Program
bash
python main.py

 How to Use
Graph 1: Effect of Velocity
Enter a fixed launch angle in degrees.
Enter different initial velocities in m/s.
Observe how the projectile trajectory changes.
Type next to move to Graph 2.
Graph 2: Effect of Launch Angle
Enter a fixed initial velocity in m/s.
Enter different launch angles in degrees.
Observe how the trajectory, maximum height, and range change.
Type done to finish the simulation.

The program displays the calculated time of flight, maximum height, and horizontal range in the terminal.

 **Expected Output**

The program generates two graphs:

Graph 1: Effect of Velocity (Fixed Angle)

Multiple projectile trajectories are displayed for different initial velocities while keeping the launch angle constant.

Graph 2: Effect of Angle (Fixed Velocity)

Multiple projectile trajectories are displayed for different launch angles while keeping the initial velocity constant.

Both graphs update as new values are entered.

 **Learning Outcomes**
Through this project, I explored:

Fundamentals of projectile motion and classical mechanics.
Implementation of mathematical equations using Python.
Working with NumPy arrays and mathematical functions.
Data visualization using Matplotlib.
Interactive plotting and real-time graph updates.
Taking user input and handling invalid inputs.
Applying programming concepts to real-world physics problems.
 Future Improvements

Some features that could be added in future versions:

Graphical user interface (GUI) using Tkinter or PyQt.
Animation showing the projectile moving along its trajectory.
Sliders to control velocity and launch angle.
Ability to save trajectory graphs as images.
Comparison of theoretical and experimental projectile motion.
Support for air resistance.
 Author

Created as a beginner-friendly Python project to explore the relationship between physics, mathematics, and programming.

 If you find this project interesting, consider giving the repository a star!

Made with Python 🐍 and a curiosity for Physics 🚀
