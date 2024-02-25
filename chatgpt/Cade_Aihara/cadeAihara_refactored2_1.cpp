#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double crateL, crateW, crateH, spaceL, spaceW, spaceH;
    double crateVOL, crateSA, crateD, spaceVOL, spaceSA, spaceD, total;

    cout << "SHIPPING CRATE" << endl;
    cout << "Enter length, width, and height of the shipping crate: ";
    cin >> crateL >> crateW >> crateH;

    crateVOL = crateL * crateW * crateH;
    crateSA = 2 * (crateL * crateW + crateL * crateH + crateW * crateH);
    crateD = sqrt(pow(crateL, 2) + pow(crateW, 2) + pow(crateH, 2));

    cout << "STORAGE SPACE" << endl;
    cout << "Enter length, width, and height of the storage space: ";
    cin >> spaceL >> spaceW >> spaceH;

    spaceVOL = spaceL * spaceW * spaceH;
    spaceSA = 2 * (spaceL * spaceW + spaceL * spaceH + spaceW * spaceH);
    spaceD = sqrt(pow(spaceL, 2) + pow(spaceW, 2) + pow(spaceH, 2));
    total = floor(spaceL / crateL) * floor(spaceW / crateW) * floor(spaceH / crateH);

    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl;
    cout << "| Type   | Length | Width  | Height | Volume     | Surface Area | Diagonal   |" << endl;
    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl;
    cout << "| Crate  | " << setw(7) << fixed << setprecision(1) << crateL << " | "
         << setw(7) << crateW << " | " << setw(7) << crateH << " | "
         << setw(11) << crateVOL << " | " << setw(13) << crateSA << " | " << setw(9) << crateD << " |" << endl;
    cout << "| Space  | " << setw(7) << spaceL << " | " << setw(7) << spaceW << " | "
         << setw(7) << spaceH << " | " << setw(11) << spaceVOL << " | "
         << setw(13) << spaceSA << " | " << setw(9) << spaceD << " |" << endl;
    cout << "+--------+--------+--------+--------+------------+--------------+----------+" << endl;
    cout << fixed << setprecision(1) << total << " crates can fit in the storage space." << endl;

    return 0;
}
