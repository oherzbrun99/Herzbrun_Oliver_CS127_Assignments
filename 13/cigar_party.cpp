#include <iostream>

std::string cigar_party(int cigars, bool is_weekend){
  if (cigars >= 40 && cigars <= 60){
    return "True";
  }
  if (is_weekend == true && cigars >= 40){
    return "True";
  }
  return "False";
}

int main() {
  std::cout << cigar_party(39, true) << '\n';
  std::cout << cigar_party(41, false);
  return 0;
}
