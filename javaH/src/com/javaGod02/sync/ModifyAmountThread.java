package com.javaGod02.sync;

public class ModifyAmountThread extends Thread{

    private CommonCalculate calc;
    private boolean addFlag;

    public ModifyAmountThread(CommonCalculate clac, boolean addFlag) {
        this.calc = clac;
        this.addFlag = addFlag;
    }
    public void run() {
        for(int loop = 0; loop < 1000; loop++) {
            if(addFlag) {
                calc.plus(1);
            } else {
                calc.minus(1);
            }
        }
    }
}
