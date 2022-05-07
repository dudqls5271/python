package com.javaGod02.sync;

public class CommonCalculate {
    private int amount;
    public CommonCalculate() {
        amount = 0;
    }
    public void plus(int value){
        synchronized (this) {
            amount += value;
        }
    }

    public void minus(int value) {
        synchronized (this) {
            amount -= value;
        }
    }

    public int getAmount() {
        return amount;
    }
}
