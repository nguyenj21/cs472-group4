#include <iostream> // Standard input/output stream
#include <iomanip> // Input/output manipulators
#include <cmath> // Math functions
using namespace std;

int main() {
    // Variables for dimensions of shipping crate and storage space
    double crateL, crateW, crateH, spaceL, spaceW, spaceH;

    // Variables for volume, surface area, and diagonal of crate and space
    double crateVOL, crateSA, crateD, spaceVOL, spaceSA, spaceD, total;

    // Prompting user for dimensions of the shipping crate
    cout << "SHIPPING CRATE" << endl;
    cout << "Enter length, width, and height of the shipping crate: ";
    cin >> crateL >> crateW >> crateH;

    // Calculating volume, surface area, and diagonal of the shipping crate
    crateVOL = crateL * crateW * crateH;
    crateSA = 2 * (crateL * crateW + crateL * crateH + crateW * crateH);
    crateD = sqrt(pow(crateL, 2) + pow(crateW, 2) + pow(crateH, 2));

    // Prompting user for dimensions of the storage space
    cout << "STORAGE SPACE" << endl;
    cout << "Enter length, width, and height of the storage space: ";
    cin >> spaceL >> spaceW >> spaceH;

    // Calculating volume, surface area, and diagonal of the storage space
    spaceVOL = spaceL * spaceW * spaceH;
    spaceSA = 2 * (spaceL * spaceW + spaceL * spaceH + spaceW * spaceH);
    spaceD = sqrt(pow(spaceL, 2) + pow(spaceW, 2) + pow(spaceH, 2));

    // Calculating total number of crates that can fit in the storage space
    total = floor(spaceL / crateL) * floor(spaceW / crateW) * floor(spaceH / crateH);

    // Outputting the table header
    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl;
    cout << "| Type   | Length | Width  | Height | Volume     | Surface Area | Diagonal   |" << endl;
    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl;

    // Outputting data for the shipping crate
    cout << "| Crate  | " << setw(7) << fixed << setprecision(1) << crateL << " | "
         << setw(7) << crateW << " | " << setw(7) << crateH << " | "
         << setw(11) << crateVOL << " | " << setw(13) << crateSA << " | " << setw(9) << crateD << " |" << endl;

    // Outputting data for the storage space
    cout << "| Space  | " << setw(7) << spaceL << " | " << setw(7) << spaceW << " | "
         << setw(7) << spaceH << " | " << setw(11) << spaceVOL << " | "
         << setw(13) << spaceSA << " | " << setw(9) << spaceD << " |" << endl;

    // Outputting the table footer
    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl;

    // Outputting the total number of crates that can fit in the storage space
    cout << fixed << setprecision(1) << total << " crates can fit in the storage space." << endl;

    return 0;
}
