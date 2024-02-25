/*
Name: C******* A*******; -; CS135-1002(Lecture); CS135-1010(Lab); Assignment 3
Description: caclulates how many crates can fit in a space when given the dimenstions of the crate and space.
Input: 6 inputs (L,W,H of crate and L,W,H of space)
Output: table with input dimensions and caculations of volume, surface area, and diagonal length. also tells you how many crates can fit in the storage space.
*/

#include <iostream> //basic library
#include <iomanip> //allows us to manipulate values
#include <cmath> //allows us to use math functions
using namespace std;
int main () {

double crateL, crateW, crateH, spaceL, spaceW, spaceH; //introducing variables (inputs)
double crateVOL, crateSA, crateD, spaceVOL, spaceSA, spaceD, total; //introducing formulas to be used

cout<<"SHIPPING CRATE"<<endl;
cout<<"Enter length of shipping crate"<<endl; //asking user for dimensions
cout<<"**";
cin>>crateL;
cout<<endl;

cout<<"Enter width of shipping crate"<<endl;
cout<<"**";
cin>>crateW;
cout<<endl;

cout<<"Enter height of shipping crate"<<endl;
cout<<"**";
cin>>crateH;
cout<<endl;

	crateVOL= crateL * crateW * crateH; //assigning math functions to variables
	crateSA= 2 * (crateL *crateW +crateL *crateH +crateW *crateH);
	crateD= sqrt(pow(crateL,2)+pow(crateW,2)+pow(crateH,2));

cout<<"STORAGE SPACE"<<endl;
cout<<"Enter length of storage space"<<endl; //asking for more dimensions
cout<<"**";
cin>>spaceL;
cout<<endl;

cout<<"Enter width of storage space"<<endl;
cout<<"**";
cin>>spaceW;
cout<<endl;

cout<<"Enter height of storage space"<<endl;
cout<<"**";
cin>>spaceH;
cout<<endl;
cout<<endl;

	spaceVOL= spaceL * spaceW * spaceH; //assigning math functions to more variables
        spaceSA= 2 * (spaceL *spaceW +spaceL *spaceH +spaceW *spaceH);
        spaceD= sqrt(pow(spaceL,2)+pow(spaceW,2)+pow(spaceH,2));
	total= floor(spaceL/crateL) * floor(spaceW/crateW) * floor(spaceH/crateH);

cout<<"+--------+--------+--------+--------+------------+--------------+----------+"<<endl; //printing the table
cout<<"| Type   | Length | Width  | Height | Volume     | Surface Area | Diagonal |"<<endl;
cout<<"+--------+--------+--------+--------+------------+--------------+----------+"<<endl;
cout<<"| Crate  | ";
	cout<<setw(7)<<left<<fixed<<showpoint<<setprecision(1)<<crateL<<"| "; //creating the first row of outputs
	cout<<setw(7)<<left<<fixed<<showpoint<<setprecision(1)<<crateW<<"| ";
	cout<<setw(7)<<left<<fixed<<showpoint<<setprecision(1)<<crateH<<"| ";
	cout<<setw(11)<<left<<fixed<<showpoint<<setprecision(1)<<crateVOL<<"| ";
	cout<<setw(13)<<left<<fixed<<showpoint<<setprecision(1)<<crateSA<<"| ";
	cout<<setw(9)<<left<<fixed<<showpoint<<setprecision(1)<<crateD<<"|"<<endl;

cout<<"| Space  | ";
        cout<<setw(7)<<left<<fixed<<showpoint<<setprecision(1)<<spaceL<<"| "; //creating second row of outputs
        cout<<setw(7)<<left<<fixed<<showpoint<<setprecision(1)<<spaceW<<"| ";
        cout<<setw(7)<<left<<fixed<<showpoint<<setprecision(1)<<spaceH<<"| ";
        cout<<setw(11)<<left<<fixed<<showpoint<<setprecision(1)<<spaceVOL<<"| ";
        cout<<setw(13)<<left<<fixed<<showpoint<<setprecision(1)<<spaceSA<<"| ";
        cout<<setw(9)<<left<<fixed<<showpoint<<setprecision(1)<<spaceD<<"|"<<endl;

cout<<"+--------+--------+--------+--------+------------+--------------+----------+"<<endl;
cout<<endl;
cout<<fixed<<showpoint<<setprecision(1)<<total<<" crates can fit in the storage space."<<endl; //tells us hwo many crates fit in the storage
cout<<endl;

}
