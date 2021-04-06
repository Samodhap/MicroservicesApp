package com.example.apigw.filters;

import com.netflix.zuul.ZuulFilter;

/**
 * Created by Samodha Pallewatta on 3/26/2021.
 */
public class ErrorFilter extends ZuulFilter {
    @Override
    public String filterType() {
        return "route";
    }

    @Override
    public int filterOrder() {
        return 1;
    }

    @Override
    public boolean shouldFilter() {
        return true;
    }

    @Override
    public Object run() {
        System.out.println("Inside Route Filter");
        return null;
    }
}
