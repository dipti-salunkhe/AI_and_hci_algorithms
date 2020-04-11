#include<iostream>
#include<cstdio>
using namespace std;



int calcCost (int ArrayOfCities[], const int NUM_CITIES) 
{
	int c = 0;
	for (int i = 0; i < NUM_CITIES; ++i)
	{
		for (int j = i + 1; j < NUM_CITIES; ++j)
		{
			if (ArrayOfCities[j] < ArrayOfCities[i])
			{
				c++;
			}
		}
	}
	return c;
}

void SwapElements (int ArrayOfCities[], int i, int j)
{
	int temp = ArrayOfCities[i];
	ArrayOfCities[i] = ArrayOfCities[j];
	ArrayOfCities[j] = temp;
}

int main()
{
	const int CITIES = 8;
	int iIndex = 1;
	int ArrayOfCities[CITIES];

	for (int i = 0; i < CITIES; ++i)
	{
		cout << "Enter distance for city " << iIndex << endl;
		cin >> ArrayOfCities[i];
		++iIndex;
	}

	int bestCost = calcCost(ArrayOfCities, CITIES);
	int iNewCost = 0, iSwaps = 0;
	while (bestCost > 0) 
	{
		for (int i = 0; i < CITIES - 1; ++i)
		{
			SwapElements(ArrayOfCities, i, i + 1);
			iNewCost = calcCost(ArrayOfCities, CITIES);
			if (bestCost > iNewCost)
			{
				++iSwaps;
				cout << "Performing Swap: " << iSwaps << endl;
				for (int i = 0; i < CITIES; ++i)
				{
					cout << ArrayOfCities[i] << "->";
				}

				cout << "\n";
				bestCost = iNewCost;
			}
			else
			{
				SwapElements(ArrayOfCities, i, i + 1);
			}
		}
	}
	
	cout << "\nFinal Route: \n";
	for (int i = 0; i < CITIES; i++)
	{
		cout << ArrayOfCities[i] << endl;
	}
}

/*
Enter distance for city 1
5
Enter distance for city 2
25
Enter distance for city 3
15
Enter distance for city 4
2 
Enter distance for city 5
3
Enter distance for city 6
1
Enter distance for city 7
9
Enter distance for city 8
10
Performing Swap: 1
5->15->25->2->3->1->9->10->
Performing Swap: 2
5->15->2->25->3->1->9->10->
Performing Swap: 3
5->15->2->3->25->1->9->10->
Performing Swap: 4
5->15->2->3->1->25->9->10->
Performing Swap: 5
5->15->2->3->1->9->25->10->
Performing Swap: 6
5->15->2->3->1->9->10->25->
Performing Swap: 7
5->2->15->3->1->9->10->25->
Performing Swap: 8
5->2->3->15->1->9->10->25->
Performing Swap: 9
5->2->3->1->15->9->10->25->
Performing Swap: 10
5->2->3->1->9->15->10->25->
Performing Swap: 11
5->2->3->1->9->10->15->25->
Performing Swap: 12
2->5->3->1->9->10->15->25->
Performing Swap: 13
2->3->5->1->9->10->15->25->
Performing Swap: 14
2->3->1->5->9->10->15->25->
Performing Swap: 15
2->1->3->5->9->10->15->25->
Performing Swap: 16
1->2->3->5->9->10->15->25->

Final Route: 
1
2
3
5
9
10
15
25
*/
