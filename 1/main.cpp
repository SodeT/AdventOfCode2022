#include <fstream>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <vector>

std::string chomp(std::string input, std::string forbiddenChars)
{
    std::string output = "";
    for (size_t i = 0; i < input.length(); i++)
    {
        if (forbiddenChars.find(input[i]) == std::string::npos)
        {
            output += input[i];
        }
    }

    return output;
}

std::string readFile(std::string path)
{

    std::string output;
    std::string fileLine;
    std::fstream fileStream;
    
    fileStream.open(path, std::ios::in); 
    if (fileStream.is_open())
    { 
        while (std::getline(fileStream, fileLine))
        {  
            output.append(fileLine + '\n');
        }
        fileStream.close();   
    }
    else 
    {
        printf("Error reading file: \"%s\", aborting...\n", path.c_str());
        
        exit(1);
    }
    return output;
}

int main(void)
{
    std::string input = readFile("input.txt");
    //std::cout << input;

    std::vector<int> elfesCals;
    std::string currentLine;

    int currentElfCal = 0;
    do
    {
        currentLine = input.substr(0, input.find('\n') +1);
        input = input.substr(currentLine.length()); // remove the line we just read

        currentLine = chomp(currentLine, "\n\r ");

        if (currentLine == "")
        {
            elfesCals.push_back(currentElfCal);
            currentElfCal = 0;
        }
        else
        {
            currentElfCal += std::stoi(currentLine);
        }

    } while(input.length() > 0);

    int largest = 0;

    for (size_t i = 0; i < elfesCals.size(); i++)
    {
        if (elfesCals[i] > largest)
        {
            largest = elfesCals[i];
        }
    }   
    

    std::cout << largest << "\n";

    return 0;
}