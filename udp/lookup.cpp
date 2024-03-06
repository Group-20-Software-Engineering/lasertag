#include <iostream>
#include <unordered_map>
#include <variant>
#include <string>


//Defines the variable type to accept anything
using ValueVariant = std::variant<int, std::string, double>;
//Defines the Lookup table type
using LookupTable = std::unordered_map<std::string, ValueVariant>;


//add a key-value pair to the lookup table
void lookuptableAdd(LookupTable& table, const std::string& key, const ValueVariant& value) {
    table[key] = value;
}



