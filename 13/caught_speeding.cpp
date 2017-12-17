
#include <iostream>

std::string caught_speeding(int speed, bool is_birthday){
  if (is_birthday == true){
    speed = speed - 5;
  }
  if (speed <= 60){
    return "0";
  }
  if (speed > 60 && speed <= 80){
    return "1";
  }
  if (speed >= 81){
    return "2";
  }
  return 0;
}

int main(){
  std::cout << caught_speeding(80, false);
  return 0;
}
