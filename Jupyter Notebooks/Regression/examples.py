# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 07:54:19 2020

@author: javier.perez-alvaro
"""

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact

#### INTRODUCTION TO LINEAR MODELS 
def interactive_example(x,y):
    m = len(x)
    X = np.ones((m,2))
    X[:,1] = x
    def plot_model(a,b):
        # plot dataset
        plt.figure(figsize=(10,5))
        plt.plot(x,y,'o',label='data')
        plt.xlim([-1,1])
        plt.ylim([-1.5,3.5])
        plt.xlabel('x',fontsize=20)
        plt.ylabel('y',fontsize=20)
        # plot line
        coeffs = np.array([b,a])
        plot_range = [-2,2]
        m_plot = 100
        x_plot = plot_range[0] + (plot_range[1] - plot_range[0] ) * np.random.rand(m_plot)
        X_plot = np.ones((m_plot,2))
        X_plot[:,1] = x_plot
        y_plot = X_plot.dot(coeffs)
        plt.plot(x_plot,y_plot,'r',label='linear model')
        plt.legend(fontsize=20)
        # join points witht line
        #for i in range(m):
        #    plt.plot([x[i],x[i]],[y[i],coeffs[1]*x[i]+coeffs[0]], 'k-.')

        # mean squared error 
        #MSE = np.linalg.norm(y-X.dot(coeffs))/m
        MSE = np.sum((y-X.dot(coeffs))**2)/m
        MSE = MSE.round(2)
        plt.title('MSE = '+str(MSE),fontsize=30)
    a_s = widgets.FloatText(min=-5, max=5, step = 0.1, value=-1, description='theta1 (slope)')
    b_s = widgets.FloatText(min=-10, max=10, step = 0.1, value=0, description='theta0 (bias)')
    interact(plot_model,a=a_s,b=b_s)
    
def plot_mse(x,y):
    
    # feature matrix
    m = len(x)
    X = np.ones((m,2))
    X[:,1] = x
    
    # grid
    ms = np.linspace(-7, 10, 500)
    bs = np.linspace(-7, 10, 500)
    Ms, Bs = np.meshgrid(ms, bs)
    
    # evaluate mse at grid points
    params = np.c_[Ms.ravel(), Bs.ravel()].T
    mse = np.sum((X@params-y[:,None])**2,axis=0)/m
    mse = mse.reshape(Ms.shape)
    
    # prepare figure
    import matplotlib.colors as colors
    my_log_cm = colors.LogNorm(vmin=0.01,vmax=100)  
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(15,5))
    from matplotlib import cm
    
    # contour plot
    ax0 = fig.add_subplot(1,2,2)
    levels = np.logspace(-2,3,20)
    fig1 = ax0.contourf(Ms,Bs,mse,levels,alpha=0.9,cmap=cm.coolwarm,norm=my_log_cm)
    fig.colorbar(fig1, ticks=[1e-2,1e-1,1,10,100,1000])
    ax0.set_xlabel(r'$\theta_0$',fontsize=20)
    ax0.set_ylabel(r'$\theta_1$',fontsize=20)
    ax0.contour(Ms,Bs,mse,levels,cmap=cm.coolwarm,norm=my_log_cm)
    ax0.set_title('Contour plot',fontsize=20)
    ax0.grid()
    
    # mse plot
    ax1 = fig.add_subplot(1,2,1, projection='3d')
    surf = ax1.plot_surface(Ms, Bs, mse,cmap=cm.coolwarm,norm=my_log_cm)
    ax1.set_xlim([-5,10])
    ax1.set_ylim([-5,10])
    ax1.set_xlabel(r'$\theta_0$',fontsize=20)
    ax1.set_ylabel(r'$\theta_1$',fontsize=20)
    ax1.set_zlabel(r'MSE',fontsize=20)
    ax1.set_title('Mean Squared Error',fontsize=20)
    plt.tight_layout()
    
def interactive_prediction(x,y):
    m = len(x)
    X = np.ones((m,2))
    X[:,1] = x
    theta = np.linalg.lstsq(X,y,rcond=None)[0]
    def plot_prediction(x_new):
        
        # plot dataset
        plt.figure(figsize=(12,7))
        plt.plot(x,y,'o',label='data')
        plt.xlim([-1.5,1.5])
        plt.ylim([-2,4])
        # plot linear model
        
        plot_range = [-2,2]
        m_plot = 100
        x_plot = plot_range[0] + (plot_range[1] - plot_range[0] ) * np.random.rand(m_plot)
        X_plot = np.ones((m_plot,2))
        X_plot[:,1] = x_plot
        y_plot = X_plot.dot(theta)
        plt.plot(x_plot,y_plot,'r',label='linear model')
        plt.legend(fontsize=20)
        plt.xlabel('x',fontsize=20)
        plt.ylabel('y',fontsize=20)
        
        # plot prediction
        y_new = theta[1]*x_new+theta[0]
        plt.plot(x_new,y_new,
                 marker='o',
                 markersize = '15',
                 mec='salmon',
                 mew=2,
                 mfc='none')
        plt.plot([x_new,x_new,-1.5],[-2,y_new,y_new],'o--',color='salmon')
        plt.text(x = x_new+0.1,
                 y = -1.75,
                 s = 'new point: '+str(x_new),
                 fontsize=15)
        plt.text(x = -1.4,
                 y = y_new+0.2,
                 s = 'prediction: \n'+str(y_new.round(2)),
                 fontsize=15)

    x_new_s = widgets.FloatSlider(min=-1.5, max=1.5, step = 0.1, value=0, description='new point')
    interact(plot_prediction,x_new=x_new_s)


#### ADDING POLYNOMIAL FEATURES
def interactive_polynomial_model(x,y):
    degree_widget = widgets.IntText(value=0,min=0,max=100,step=1,description='model degree')
    def plot_model(degree):
        m = len(x)
        m_plot = 200
        x_plot = np.linspace(-1,1,m_plot)        
        X_plot = np.ones((m_plot,1))
        X = np.ones((m,1))
        for i in range(degree):
            X = np.c_[X,x**(i+1)]
            X_plot = np.c_[X_plot,x_plot**(i+1)]
        
        theta = np.linalg.lstsq(X,y,rcond=None)[0]
        y_plot = X_plot.dot(theta)
        
        plt.figure(figsize=(12,5))
        plt.plot(x,y,'o')
        plt.xlim([-1,1])
        plt.ylim([-5,6])
        plt.plot(x_plot,y_plot,'r',label='linear model')
        'Mean Squared Error'
        MSE = np.sum((y-X.dot(theta))**2)/m
        print('Mean Squared Error: '+str(MSE))
    interact(plot_model,degree=degree_widget)