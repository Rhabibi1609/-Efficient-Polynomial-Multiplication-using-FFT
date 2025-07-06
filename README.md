
# Polynomial Evaluation and Multiplication using FFT

## Overview

This project implements efficient polynomial evaluation and multiplication using the Fast Fourier Transform (FFT) in Python. Traditional polynomial operations have a time complexity of O(n²), while FFT-based methods reduce this to O(n log n).

The project is divided into three main tasks:

- **Task 1:** Evaluate a polynomial using Horner's rule as a baseline (O(n²)).
- **Task 2:** Implement the FFT and inverse FFT (IFFT) to evaluate polynomials and recover coefficients.
- **Task 3:** Multiply polynomials using FFT-based convolution for significant performance improvement.

---

## Program Design

The program reads polynomial coefficients from input files, performs specified operations (evaluation, FFT, multiplication), and writes results to output files. All main tasks are modularized into separate functions for better readability and maintenance.

---

## How to Run

1. Place your input files in the same directory as `Project.py`.
2. Run the program:
   ```bash
   python Project.py
   ```
3. Follow the prompts to provide input file names for each task.

---

## Task Workflows

### 1. Horner’s Rule Evaluation

```mermaid
graph LR
    A[Polynomial Coefficients]
    B[Iterative Evaluation (O(n²))]
    C[Final Evaluated Value]

    A --> B --> C
```

---

### 2. FFT Recursive Flow

```mermaid
graph TD
    A[Input Polynomial Coefficients]
    B[Split into Even and Odd Indices]
    C[FFT on Even Coefficients (Recursion)]
    D[FFT on Odd Coefficients (Recursion)]
    E[Combine with Roots of Unity]
    F[Frequency Domain Representation]

    A --> B
    B --> C
    B --> D
    C --> E
    D --> E
    E --> F
```

---

### 3. Polynomial Multiplication using FFT

```mermaid
graph LR
    A[Polynomial A]
    B[Polynomial B]
    C[FFT(A)]
    D[FFT(B)]
    E[Point-wise Multiply FFTs]
    F[Inverse FFT of Product]
    G[Final Product Polynomial]

    A --> C
    B --> D
    C --> E
    D --> E
    E --> F
    F --> G
```

---

## Implementation Highlights

- Recursive FFT and IFFT implementations using divide-and-conquer.
- Complex arithmetic managed with Python's `cmath`.
- Zero-padding to nearest power of two for input sizes.
- Modular design: separate functions for evaluation, FFT, IFFT, multiplication.

---

## Known Limitations

- Input files must be correctly formatted.
- The first number in input lines is treated as real part, the second as imaginary.
- Sign issues may occur with zero coefficients in output.

---

## Conclusion

This project demonstrates how FFT drastically improves polynomial operations efficiency. It provides a modular, extensible Python implementation with support for complex coefficients.

---
