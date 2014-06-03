#include <iostream>
#include <vector>

using namespace std;

// Función de lectura de vectores
template<class T>
istream& operator>> (istream& input, vector<T>& v){
    for (auto &i : v)
        input >> i;

    return input;
}

pair<unsigned, unsigned> resuelve(vector<double> precios) {
    unsigned minimo = 0,
        compra = 0,
        venta = 0;

    for (unsigned i = 1; i < precios.size(); i++) {
        if (precios[i] < precios[minimo])
            minimo = i;

        double beneficio = precios[i] - precios[minimo];

        if (beneficio > precios[venta] - precios[compra]) {
            compra = minimo;
            venta = i;
        }
    }

    return make_pair(compra, venta);
}

int main(){
    unsigned num_dias;

    // Lectura de datos del problema

    cout << "Introduce número de días: ";
    cin >> num_dias;
    vector<double> precios(num_dias);
    cout << "Introduce precios de acciones por días: ";
    cin >> precios;

    pair<unsigned, unsigned> compraventa = resuelve(precios);
    double beneficio = precios[compraventa.second] - precios[compraventa.first];


    cout << "Día de compra: " << compraventa.first << endl
         << "Día de venta: " << compraventa.second << endl
         << "Beneficio: " << beneficio << endl;
}
