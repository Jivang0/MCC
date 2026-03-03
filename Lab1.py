#1.	Lab 1: Number System and Binary Arithmetic (2 Hours)
# Decimal to Binary, Octal, Hexadecimal


# num = int(input("Enter a decimal number: "))
# print("Binary:", bin(num))
# print("Octal:", oct(num))
# print("Hexadecimal:", hex(num))



# Binary, Octal, Hexadecimal to Decimal
# binary = input("Enter a binary number: ")
# octal = input("Enter an octal number: ")
# hexa = input("Enter a hexadecimal number: ")

# print("Binary to Decimal:", int(binary, 2))
# print("Octal to Decimal:", int(octal, 8))
# print("Hexadecimal to Decimal:", int(hexa, 16))



# Binary Addition (Manual)
# a = input("Enter first binary number: ")
# b = input("Enter second binary number: ")
# # Convert to decimal, add, convert back
# result = int(a, 2) + int(b, 2)
# print("Addition Result:", bin(result)[2:])


# Binary Subtraction
# a = input("Enter first binary number: ")
# b = input("Enter second binary number: ")
# result = int(a, 2) - int(b, 2)
# print("Subtraction Result:", bin(result)[2:])


#	1’s and 2’s complement subtraction

#1’s Complement Subtraction
#steps
#Take 1’s complement of subtrahend
# Add to minuend
# If carry → add carry to result

# 1's Complement
def ones_complement(binary):
    result = ""
    for bit in binary:
        if bit == '0':
            result += '1'
        else:
            result += '0'
    return result

a = input("Enter minuend (binary): ")
b = input("Enter subtrahend (binary): ")

b_complement = ones_complement(b)

result = bin(int(a,2) + int(b_complement,2))[2:]

print("1's Complement Result:", result)

# 2’s Complement Subtraction
# Steps:
# Take 1’s complement
# Add 1
# Add to minuend
# 2's Complement

def twos_complement(binary):
    ones = ""
    for bit in binary:
        if bit == '0':
            ones += '1'
        else:
            ones += '0'
    twos = bin(int(ones,2) + 1)[2:]
    return twos

a = input("Enter minuend (binary): ")
b = input("Enter subtrahend (binary): ")

b_twos = twos_complement(b)

result = bin(int(a,2) + int(b_twos,2))[2:]

print("2's Complement Result:", result)


# Verification Using Built-in Functions
a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

print("Addition (verified):", bin(int(a,2) + int(b,2)))
print("Subtraction (verified):", bin(int(a,2) - int(b,2)))


# Lab 2: Set Operations using Python / Excel
# Set Operations in Python
# Program for Union, Intersection, Difference, Symmetric Difference 
# Input sets

A = set(map(int, input("Enter elements of Set A (space separated): ").split()))
B = set(map(int, input("Enter elements of Set B (space separated): ").split()))
# Input Examle:
# A = {1,2,3,4}
# B = {3,4,5,6}

#output Example:j
# Union = {1,2,3,4,5,6}
# Intersection = {3,4}
# A-B = {1,2}
# B-A = {5,6}
# Symmetric Difference = {1,2,5,6}

print("Set A:", A)
print("Set B:", B)

# Union
print("Union (A ∪ B):", A | B)

# Intersection
print("Intersection (A ∩ B):", A & B)

# Difference
print("Difference (A - B):", A - B)
print("Difference (B - A):", B - A)

# Symmetric Difference
print("Symmetric Difference (A Δ B):", A ^ B)


# De Morgan’s Laws Validation
#  De Morgan’s Laws:
# (A ∪ B)' = A' ∩ B'
# (A ∩ B)' = A' ∪ B'

U = set(range(1, 11))  # Universal set {1 to 10}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Complements
A_comp = U - A
B_comp = U - B

# Law 1
left1 = U - (A | B)
right1 = A_comp & B_comp

print("Law 1 Valid:", left1 == right1)

# Law 2
left2 = U - (A & B)
right2 = A_comp | B_comp

print("Law 2 Valid:", left2 == right2)

# If both outputs are True, De Morgan’s laws are verified.

# Venn Diagram Visualization (Python)
#pip install matplotlib matplotlib-venn
from matplotlib import pyplot as plt
#from matplotlib_venn import venn2

A = {1,2,3,4}
B = {3,4,5,6}

#venn2([A, B], set_labels=('Set A', 'Set B'))

plt.title("Venn Diagram of Set A and B")
plt.show()

# Database Segmentation Case Task
# A company has:
# Set A → Customers who bought Product X
# Set B → Customers who bought Product Y

X = {"Ram", "Hari", "Sita", "Gita"}
Y = {"Hari", "Sita", "Mohan", "Rita"}

print("Customers who bought both:", X & Y)
print("Customers who bought only X:", X - Y)
print("Customers who bought only Y:", Y - X)
print("Customers who bought either:", X | Y)
print("Customers who bought only one product:", X ^ Y)



# Lab 3: Relations & Functions Visualization (3 Hours)
# Matrix Representation of Relation
A = [1, 2, 3]
R = [(1,1), (1,2), (2,2), (3,3)]

n = len(A)
matrix = [[0]*n for _ in range(n)]

for (a,b) in R:
    i = A.index(a)
    j = A.index(b)
    matrix[i][j] = 1

print("Relation Matrix:")
for row in matrix:
    print(row)

# Check Reflexive, Symmetric, Transitive
#Reflexive
# A relation is reflexive if (a,a) ∈ R for all a ∈ A.
def is_reflexive(A, R):
    for a in A:
        if (a,a) not in R:
            return False
    return True

# Symmetric
# If (a,b) ∈ R then (b,a) ∈ R.
def is_symmetric(R):
    for (a,b) in R:
        if (b,a) not in R:
            return False
    return True

# Transitive
# If (a,b) and (b,c) ∈ R then (a,c) must be in R.
def is_transitive(R):
    for (a,b) in R:
        for (c,d) in R:
            if b == c and (a,d) not in R:
                return False
    return True

# Complete Check Program
print("Reflexive:", is_reflexive(A,R))
print("Symmetric:", is_symmetric(R))
print("Transitive:", is_transitive(R))

# Plot Functions (GeoGebra / MATLAB)
# A. MATLAB Code
# Linear Function
# y = 2x + 1
x = -10:0.1:10;
y = 2*x + 1;
plot(x,y)
title('Linear Function')
grid on

# Quadratic Function
# y = x²
y = x.^2;
plot(x,y)
title('Quadratic Function')
grid on

# Exponential Function
# y = e^x
y = exp(x);
plot(x,y)
title('Exponential Function')
grid on

# Logarithmic Function
# y = log(x)
x = 0.1:0.1:10;
y = log(x);
plot(x,y)
title('Logarithmic Function')
grid on

# B. GeoGebra Input
# Just type in GeoGebra:
f(x) = 2x + 1
g(x) = x^2
h(x) = e^x
k(x) = log(x)


# Graph Transformations

# Vertical Shift
# f(x) = x²
# g(x) = x² + 3 → Shift up 3 units

# Horizontal Shift
# g(x) = (x - 2)² → Shift right 2 units

# Reflection
# g(x) = -x² → Reflect over x-axis
# g(x) = f(-x) → Reflect over y-axis

# Stretch / Compression
# g(x) = 2x² → Vertical stretch
# g(x) = x²/2 → Vertical compression

# MATLAB Example for Transformation
x = -10:0.1:10;
y1 = x.^2;
y2 = (x-2).^2;
y3 = x.^2 + 3;

plot(x,y1, x,y2, x,y3)
legend('x^2','(x-2)^2','x^2+3')
grid on

#	Lab 4: Matrix Operations & System Solving (3 Hours)
# Matrix Operations & System Solving (3 Hours)
# Matrix arithmetic using NumPy/Matlab

import numpy as np

# Define matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition
print("A + B:\n", A + B)

# Subtraction
print("A - B:\n", A - B)

# Multiplication (Matrix multiplication)
print("A * B:\n", np.dot(A, B))

# Transpose
print("Transpose of A:\n", A.T)

# Using MATLAB
A = [1 2; 3 4];
B = [5 6; 7 8];
A + B
A - B
A * B
A'

# Determinant & Inverse Calculation
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

# Determinant
det = np.linalg.det(A)
print("Determinant:", det)

# Inverse
if det != 0:
    inv = np.linalg.inv(A)
    print("Inverse:\n", inv)
else:
    print("Matrix is singular (no inverse)")

# MATLAB
det(A)
inv(A)

# Solving System using Gaussian Elimination

# Example System
# 2x + y = 5
# 4x + 3y = 11

# Python Implementation (Manual Gaussian Elimination)
import numpy as np

# Augmented matrix
A = np.array([[2, 1, 5],
              [4, 3, 11]], dtype=float)

n = len(A)

# Forward elimination
for i in range(n):
    for j in range(i+1, n):
        ratio = A[j][i] / A[i][i]
        A[j] = A[j] - ratio * A[i]

# Back substitution
x = np.zeros(n)

for i in range(n-1, -1, -1):
    x[i] = A[i][n]
    for j in range(i+1, n):
        x[i] -= A[i][j] * x[j]
    x[i] /= A[i][i]

print("Solution:", x)

# Using NumPy Built-in (Verification)
coeff = np.array([[2,1],
                  [4,3]])

const = np.array([5,11])

solution = np.linalg.solve(coeff, const)
print("Verified Solution:", solution)

# Simple Networking Application (Using Matrices)
# 📌 Example: Network Adjacency Matrix
# Suppose we have 3 computers:
# Computer 1 connected to 2
# Computer 2 connected to 3
# Adjacency Matrix:

#Python Example
import numpy as np

# Adjacency matrix
network = np.array([[0,1,0],
                    [1,0,1],
                    [0,1,0]])

print("Network Adjacency Matrix:\n", network)

# Check number of connections for each computer
connections = np.sum(network, axis=1)
print("Connections per node:", connections)

# Lab 5: Vector Algebra & Cross Product (3 Hours)
# Dot and cross product computation
# Linear combination & span
# Rank-based independence test
# Vector visualization

#Dot Product & Cross Product
import numpy as np

# Define vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Dot Product
dot_product = np.dot(A, B)

# Cross Product
cross_product = np.cross(A, B)

print("Vector A:", A)
print("Vector B:", B)
print("Dot Product:", dot_product)
print("Cross Product:", cross_product)

# Linear Combination & Span Check
# Define vectors in R2
v1 = np.array([1, 0])
v2 = np.array([0, 1])

# Target vector
v = np.array([3, 4])

# Solve c1*v1 + c2*v2 = v
coefficients = np.linalg.solve(np.column_stack((v1, v2)), v)

print("Target Vector:", v)
print("Coefficients:", coefficients)
print("Verification:", coefficients[0]*v1 + coefficients[1]*v2)

# Rank-Based Independence Test
# Define vectors
v1 = [1, 2, 3]
v2 = [2, 4, 6]
v3 = [1, 1, 1]

# Form matrix
matrix = np.array([v1, v2, v3])

# Calculate rank
rank = np.linalg.matrix_rank(matrix)

print("Matrix:\n", matrix)
print("Rank:", rank)

if rank == len(matrix):
    print("Vectors are Linearly Independent")
else:
    print("Vectors are Linearly Dependent")

# Vector Visualization (2D)
import matplotlib.pyplot as plt

v1 = np.array([2, 3])
v2 = np.array([4, 1])

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1)
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1)

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.grid()
plt.title("2D Vector Visualization")
plt.show()

# Vector Visualization (3D + Cross Product)
from mpl_toolkits.mplot3d import Axes3D

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.cross(A, B)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
ax.quiver(0, 0, 0, A[0], A[1], A[2])
ax.quiver(0, 0, 0, B[0], B[1], B[2])
ax.quiver(0, 0, 0, C[0], C[1], C[2])

ax.set_xlim([0, 7])
ax.set_ylim([0, 7])
ax.set_zlim([0, 7])

ax.set_title("3D Vector & Cross Product Visualization")
plt.show()

# Lab 6: IT Applications Mini Project (3 Hours)
# Lab Objective
# To integrate mathematical concepts into real-world computing applications and develop a working mini project with presentation and report.
# Mini Project Option 1: Password Security Analyzer (Mathematics + Security)
# Mathematical Concepts Used
# Permutations & Combinations
# Entropy (Information Theory)
# Logarithm
# Probability
# Python Implementation

import math
import string

def password_entropy(password):
    length = len(password)

    # Character pool detection
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += 32

    entropy = length * math.log2(pool)
    return entropy

password = input("Enter password: ")
entropy = password_entropy(password)

print("Entropy:", round(entropy,2), "bits")

if entropy < 40:
    print("Weak Password")
elif entropy < 60:
    print("Moderate Password")
else:
    print("Strong Password")

# Mini Project Option 2: 3D Transformation Simulator (Computer Graphics)
# Mathematical Concepts
# Matrix multiplication
# Rotation matrix
# Translation
# Scaling
import numpy as np
import math

# Define point
point = np.array([1, 1, 1])

theta = math.radians(45)

rotation_z = np.array([
    [math.cos(theta), -math.sin(theta), 0],
    [math.sin(theta),  math.cos(theta), 0],
    [0, 0, 1]
])

rotated_point = np.dot(rotation_z, point)

print("Original Point:", point)
print("Rotated Point:", rotated_point)

# Mini Project Option 3: Relational Mapping System (Discrete Mathematics)
# Mathematical Concept
# Relations
# Cartesian product
# Function mapping
# Graph representation
students = ["A", "B", "C"]
courses = ["Math", "AI", "Graphics"]

# Relation (Student, Course)
relation = [("A", "Math"), ("B", "AI"), ("C", "Graphics")]

print("Relation R:")
for pair in relation:
    print(pair)

# Check if function
student_set = set()
is_function = True

for s, c in relation:
    if s in student_set:
        is_function = False
        break
    student_set.add(s)

print("Is Function:", is_function)

# Mini Project Option 4: Simple Cryptographic Modeling (Caesar Cipher + Modular Arithmetic)
#  Mathematical Concept
def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = (ord(char.lower()) - 97 + key) % 26
            result += chr(shift + 97)
        else:
            result += char
    return result

text = input("Enter message: ")
key = 3

encrypted = caesar_encrypt(text, key)

print("Encrypted:", encrypted)