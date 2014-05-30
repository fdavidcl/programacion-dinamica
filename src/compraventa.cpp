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

typedef unsigned int uint;
typedef struct{
    uint dia_compra;
    double beneficio;
} Transaccion;

// Cotización de las acciones
vector<double> precios;
// Vector de compraventas donde el índice es el día de venta
vector<Transaccion> beneficios;


Transaccion resuelve(uint dia){
    if (beneficios.size() <= dia){
        if (dia == 0)
            beneficios.push_back({0,0});
        else{
            double actual = resuelve(dia-1).beneficio + precios[dia] - precios[dia-1];
            if (actual < 0)
                beneficios.push_back({dia,0});
            else
                beneficios.push_back({resuelve(dia-1).dia_compra, actual});
        }
    }
    return beneficios[dia];
}

int main(){
    uint num_dias;
    uint max_index(0);
    
    // Lectura de datos del problema
    cout << "Introduce número de días: ";
    cin >> num_dias;
    precios.resize(num_dias);
    cout << "Introduce precios de acciones por días: ";
    cin >> precios;
    
    resuelve(num_dias-1);
    
    for (uint i = 1; i < beneficios.size(); ++i){
        if (beneficios[i].beneficio > beneficios[max_index].beneficio)
            max_index = i;
    }
    
    cout << "Día de compra: " << beneficios.at(max_index).dia_compra << endl
         << "Día de venta: " << max_index << endl;
}