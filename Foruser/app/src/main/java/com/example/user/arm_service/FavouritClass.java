package com.example.user.arm_service;

import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.time.Instant;

/**
 * Created by User on 26.09.2018.
 */

public class FavouritClass extends Fragment {
    public FavouritClass(){

    }
    public static FavouritClass newInstance(){
        return new FavouritClass();
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        return inflater.inflate(R.layout.fragment_favourit, container, false);
    }
}
