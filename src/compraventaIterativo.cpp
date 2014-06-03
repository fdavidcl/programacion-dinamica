#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Función de lectura de vectores
template<class T>
istream& operator>> (istream& input, vector<T>& v){
    for (auto &i : v)
        input >> i;

    return input;
}

// Cambio en el struct: Ahora lleva el día de compra y de venta, y calculamos el beneficio a partir de estos datos.
typedef struct{
    unsigned dia_compra;
    unsigned dia_venta;
} Transaccion;

Transaccion resuelve(vector<double> precios){
    unsigned dias = precios.size();
    double minimo = precios[0];
    double max_beneficio = 0;               // Asumimos que el beneficio inicial es 0
    int min_index = 0;
    int indice_compra = 0;
    int max_index = 0;

    for (unsigned i = 1; i < dias; i++){
        // Actualizamos el mínimo
        if (precios[i] < minimo){
            minimo = precios[i];
            min_index = i;
        }

        double beneficio = precios[i] - minimo;

        // Si el beneficio es mayor que el mejor beneficio hasta el momento, actualizamos los índices.
        if (beneficio > max_beneficio){
            indice_compra = min_index;
            max_beneficio = beneficio;
            max_index = i;
        }
    }
    Transaccion venta;
    venta.dia_compra = indice_compra;
    venta.dia_venta = max_index;
    return venta;
}

int main(){
    unsigned num_dias;

    // Lectura de datos del problema

    cout << "Introduce número de días: ";
    cin >> num_dias;
    vector<double> precios(num_dias);
    cout << "Introduce precios de acciones por días: ";
    cin >> precios;

    Transaccion compraventa = resuelve(precios);
    double beneficio = precios[compraventa.dia_venta] - precios[compraventa.dia_compra];


    cout << "Día de compra: " << compraventa.dia_compra << endl
         << "Día de venta: " << compraventa.dia_venta << endl
         << "Beneficio: " << beneficio << endl;
}
