#include <iostream>
#include "time.h"

void Time::setTime(int hour, int min, int sec) {
    this->hour = hour;
    this->min = min;
    this->sec = sec;
}

void Time::normalizeTime() {
    min += sec / 60;
    sec %= 60;
    hour += min / 60;
    min %= 60;
}

Time operator+ (const Time& obj1, const Time& obj2) {
    Time result;
    result.sec = obj1.sec + obj2.sec;
    result.min = obj1.min + obj2.min;
    result.hour = obj1.hour + obj2.hour;
    result.normalizeTime();
    return result;
}

Time operator+ (const Time& obj1, int secs) {
    Time result = obj1;
    result.sec += secs;
    result.normalizeTime();
    return result;
}

void Time::printTime() {
    std::cout << hour << ":" << min << ":" << sec << "\n";
}

std::ostream& operator<< (std::ostream& out, const Time& obj) {
    out << obj.hour << ":" << obj.min << ":" << obj.sec;
    return out;
}
