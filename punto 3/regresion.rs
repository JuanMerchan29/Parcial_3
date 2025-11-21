fn main() {
    // Datos
    let x = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    let y = vec![2.0, 4.0, 6.0, 8.0, 10.0];

    let m = x.len() as f64;

    // Parámetros
    let mut w = 0.0;
    let mut b = 0.0;

    let learning_rate = 0.01;
    let epochs = 1000;

    for epoch in 0..epochs {
        // y_pred = w * x + b
        let y_pred: Vec<f64> = x.iter().map(|xi| w * xi + b).collect();

        // error = y_pred - y
        let error: Vec<f64> = y_pred.iter()
                                   .zip(y.iter())
                                   .map(|(yp, yi)| yp - yi)
                                   .collect();

        // dw = 2/m * sum(error * x)
        let dw: f64 = (2.0 / m) *
            error.iter()
                 .zip(x.iter())
                 .map(|(e, xi)| e * xi)
                 .sum::<f64>();

        // db = 2/m * sum(error)
        let db: f64 = (2.0 / m) * error.iter().sum::<f64>();

        // Actualización
        w -= learning_rate * dw;
        b -= learning_rate * db;

        // Mostrar cada 200 epochs
        if (epoch + 1) % 200 == 0 {
            let mse: f64 = error.iter().map(|e| e * e).sum::<f64>() / m;
            println!(
                "Epoch {}, MSE: {:.4}, w: {:.4}, b: {:.4}",
                epoch + 1,
                mse,
                w,
                b
            );
        }
    }

    println!("\nModelo entrenado:");
    println!("w ≈ {:.4}, b ≈ {:.4}", w, b);

    // Predicción final
    let x_nuevo = 7.0;
    let y_pred_nuevo = w * x_nuevo + b;
    println!("Para x = {}, y_pred ≈ {:.4}", x_nuevo, y_pred_nuevo);
}
