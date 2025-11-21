import time
import tracemalloc
import subprocess
import numpy as np


# ------------------------------
#  Python + NumPy
# ------------------------------
def python_numpy():
    X = np.array([1,2,3,4,5], dtype=float)
    Y = np.array([2,4,6,8,10], dtype=float)

    w = 0.0
    b = 0.0
    lr = 0.01
    epochs = 1000
    m = len(X)

    for _ in range(epochs):
        y_pred = w * X + b
        error = y_pred - Y
        dw = (2/m) * np.dot(error, X)
        db = (2/m) * np.sum(error)
        w -= lr * dw
        b -= lr * db


# ------------------------------
#  Python puro (sin NumPy)
# ------------------------------
def python_puro():
    X = [1.0,2.0,3.0,4.0,5.0]
    Y = [2.0,4.0,6.0,8.0,10.0]

    w = 0.0
    b = 0.0
    lr = 0.01
    epochs = 1000
    m = len(X)

    for _ in range(epochs):
        y_pred = [w*x + b for x in X]
        error = [yp - y for yp, y in zip(y_pred, Y)]
        dw = (2/m) * sum(e * x for e, x in zip(error, X))
        db = (2/m) * sum(error)
        w -= lr * dw
        b -= lr * db


# ------------------------------
#  Ejecutar el binario Rust
# ------------------------------
def rust_bin():
    # Asegúrate de compilar con:
    # cargo build --release
    subprocess.run(["./target/release/regresion"], capture_output=True)


# ------------------------------
#  Benchmark general
# ------------------------------
def medir(func):
    tracemalloc.start()
    t1 = time.perf_counter()

    func()

    t2 = time.perf_counter()
    memoria = tracemalloc.get_traced_memory()[1] / 1024
    tracemalloc.stop()

    return t2 - t1, memoria


def main():
    print("== Benchmark Regresión Lineal ==")

    t_np, mem_np = medir(python_numpy)
    print(f"Python + NumPy:  {t_np:.6f}s, {mem_np:.2f} KB")

    t_puro, mem_puro = medir(python_puro)
    print(f"Python puro:     {t_puro:.6f}s, {mem_puro:.2f} KB")

    try:
        t_rust, mem_rust = medir(rust_bin)
        print(f"Rust binario:    {t_rust:.6f}s, {mem_rust:.2f} KB")
    except FileNotFoundError:
        print("Rust aún no está compilado (cargo build --release).")


if __name__ == "__main__":
    main()
