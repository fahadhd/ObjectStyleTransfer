#include <boost/filesystem.hpp>
#include <boost/foreach.hpp>
#include <iostream>
using namespace std;



int main(){
  namespace fs = boost::filesystem;

  fs::path targetDir("TriMaps/480p/bear");

  fs::directory_iterator it(targetDir), eod;

  BOOST_FOREACH(fs::path const &p, std::make_pair(it, eod))
  {
      if(fs::is_regular_file(p))
      {
        cout << p << endl;
      }
  }
  return 0;
}
