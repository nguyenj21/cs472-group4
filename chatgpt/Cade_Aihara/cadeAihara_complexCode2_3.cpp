#include <iostream> // Including the library for standard input/output stream
#include <iomanip> // Including the library for input/output manipulators
#include <cmath> // Including the library for math functions
using namespace std;

int main() {
    double crateL, crateW, crateH, spaceL, spaceW, spaceH; // Declaring variables for dimensions of shipping crate and storage space
    double crateVOL, crateSA, crateD, spaceVOL, spaceSA, spaceD, total; // Declaring variables for volume, surface area, and diagonal of crate and space

    cout << "SHIPPING CRATE" << endl; // Prompting user for dimensions of the shipping crate
    cout << "Enter length, width, and height of the shipping crate: ";
    cin >> crateL >> crateW >> crateH; // Taking input for crate dimensions

    crateVOL = crateL * crateW * crateH; // Calculating volume of the crate
    crateSA = 2 * (crateL * crateW + crateL * crateH + crateW * crateH); // Calculating surface area of the crate
    crateD = sqrt(pow(crateL, 2) + pow(crateW, 2) + pow(crateH, 2)); // Calculating diagonal of the crate

    cout << "STORAGE SPACE" << endl; // Prompting user for dimensions of the storage space
    cout << "Enter length, width, and height of the storage space: ";
    cin >> spaceL >> spaceW >> spaceH; // Taking input for storage space dimensions

    spaceVOL = spaceL * spaceW * spaceH; // Calculating volume of the storage space
    spaceSA = 2 * (spaceL * spaceW + spaceL * spaceH + spaceW * spaceH); // Calculating surface area of the storage space
    spaceD = sqrt(pow(spaceL, 2) + pow(spaceW, 2) + pow(spaceH, 2)); // Calculating diagonal of the storage space

    total = floor(spaceL / crateL) * floor(spaceW / crateW) * floor(spaceH / crateH); // Calculating total number of crates that can fit in the storage space

    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl; // Outputting the table header
    cout << "| Type   | Length | Width  | Height | Volume     | Surface Area | Diagonal   |" << endl;
    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl;

    cout << "| Crate  | " << setw(7) << fixed << setprecision(1) << crateL << " | " // Outputting data for the shipping crate
         << setw(7) << crateW << " | " << setw(7) << crateH << " | "
         << setw(11) << crateVOL << " | " << setw(13) << crateSA << " | " << setw(9) << crateD << " |" << endl;

    cout << "| Space  | " << setw(7) << spaceL << " | " << setw(7) << spaceW << " | " // Outputting data for the storage space
         << setw(7) << spaceH << " | " << setw(11) << spaceVOL << " | "
         << setw(13) << spaceSA << " | " << setw(9) << spaceD << " |" << endl;

    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl; // Outputting the table footer

    cout << fixed << setprecision(1) << total << " crates can fit in the storage space." << endl; // Outputting the total number of crates that can fit in the storage space

    return 0;
}
