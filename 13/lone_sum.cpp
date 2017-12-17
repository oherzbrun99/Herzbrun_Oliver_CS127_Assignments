#include <iostream>

int lone_sum(int a, int b, int c){
  int ret_sum = 0;
  if ( a != b && a != c){
    ret_sum += a;
  }
  if ( b != a && b != c){
    ret_sum += b;
  }
  if ( c != b && c != a){
    ret_sum += c;
  }
  return ret_sum;}

int main(){
std::cout << lone_sum(4, 5, 6) << std::endl;
std::cout << lone_sum(8, 27, 8);
}
