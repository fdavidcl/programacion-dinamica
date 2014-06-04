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

unsigned num_coins(vector<unsigned> tipos, unsigned precio) {
    vector<unsigned> monedas(precio+1, 0);

    for (unsigned c = 0; c <= precio; c++)
        for (unsigned m : tipos)
            if (c+m <= precio &&
                (monedas[c+m] == 0 || monedas[c] + 1 < monedas[c+m]))
                monedas[c+m] = monedas[c] + 1;

    return monedas[precio];
}

int main (int argc, char const *argv[]) {
    unsigned precio, size;

    cout << "Cantidad de monedas: ";
    cin >> size;
    vector<unsigned> tipos(size);

    cout << endl << "Tipos de monedas: ";
    cin >> tipos;

    cout << endl << "Precio a conseguir: ";
    cin >> precio;

    cout << endl << "Número de monedas necesarias: " << num_coins(tipos, precio) << endl;

    return 0;
}
