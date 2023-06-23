//
// Created by yottso on 1.10.22.
//
#include "iostream"
#include "fstream"
#include "string"
#include "atm.h"
#include "windows.h"

using std::string;
using std::endl;

void UserCard::SetCardNumber(int card_number) {
  CardNumber = card_number;
}
void UserCard::SetCardHolder(string card_holder) {
  CardHolder = card_holder;
}
void UserCard::SetBalance(double balance) {
  UserCard::balance = balance;
}
void UserCard::SetPassword(int password) {
  Password = password;
}
int UserCard::GetCardNumber() const {
  return CardNumber;
}
std::string UserCard::GetCardHolder() const {
  return CardHolder;
}
int UserCard::GetPassword() const {
  return Password;
}
double UserCard::GetBalance() const {
  return balance;
}
void UserCard::InsertingCard() {
    std::ifstream CardInfo;
    CardInfo.open("card.txt");
    if(CardInfo.is_open()){
      string buff;
      getline(CardInfo, buff);
      SetCardNumber(atoi(buff.c_str()));
      getline(CardInfo, buff);
      SetPassword(atoi(buff.c_str()));
      getline(CardInfo, buff);
      SetCardHolder(buff);
      getline(CardInfo,buff);
      SetBalance(stod(buff));
    }
    CardInfo.close();
}

namespace fs = std::experimental::filesystem;

bool Atm::exists(string name){
  HANDLE fileHandle;
  WIN32_FIND_DATA ffd;
  LARGE_INTEGER szDir;
  WIN32_FIND_DATA fileData;
  fileHandle = FindFirstFile("database\\*", &ffd);

  if (INVALID_HANDLE_VALUE == fileHandle)
    printf("Invalid File Handle Value \n");

  do
  {
    if (ffd.cFileName == deleteSpaces(name)){
      return true;
    }
  } while (FindNextFile(fileHandle, &ffd) != 0);
  return false;
}

void Atm::save(string path, UserCard card) {
  fout.open("database\\"+deleteSpaces(path));
  fout<<card.GetCardNumber()<<endl<<card.GetPassword()<<endl<<card.GetCardHolder()<<endl<<card.GetBalance();
  fout.close();
}

UserCard Atm::getCardNow(){
  return cardNow;
}

void Atm::setCardNow(string path) {
  fin.open("database\\"+path);
  if(fin.is_open()){
    string buff;
    getline(fin, buff);
    cardNow.SetCardNumber(atoi(buff.c_str()));
    getline(fin, buff);
    cardNow.SetPassword(atoi(buff.c_str()));
    getline(fin, buff);
    cardNow.SetCardHolder(buff);
    getline(fin,buff);
    cardNow.SetBalance(stod(buff));
  }
  fin.close();
}

string Atm::deleteSpaces(string path) {
  string res="";
  for(int i=0; i<path.size(); i++){
    if(path[i]!=' '){
      res+=path[i];
    }
  }
  return res;
}


