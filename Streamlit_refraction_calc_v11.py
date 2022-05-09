# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:48:46 2022

@author: Kelly
"""

import streamlit as st
import pandas as pd
import numpy as np
import math
import PIL
from PIL import Image


st.markdown(
    """
    <style>
    .main {
        background-color: #FFFFFF;
        }
    <style>
    """,
    unsafe_allow_html=True)


header = st.container()
angle_of_incidence= st.container()
substance_1 = st.container()
substance_2 = st.container()
substance_3 = st.container()
refraction_boundaries = st.container()
substance_test = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

RI_Dict = {
     'Acetone': 1.360000, 'Acrylic Glass': 1.491000, 'Air': 1.000293, 'Amber' : 1.550000, 
     'Benzene': 1.501000, 'Bromine': 1.661000, 'Carbon Dioxide': 1.001000, 
     'Corn Oil': 1.470000, 'Crown Glass (pure)': 1.520000, 'Cubic Zirconia': 2.165000, 
     'Diamond': 2.417000, 'Ethanol': 1.361000, 'Film (transparent)': 1.400000, 'Flint Glass (pure)': 1.610000, 'Germanium': 4.070000, 
     'Glycerol': 1.472900, 'Helium': 1.000036, 'Hydrogen': 1.000132, 'Kerosene': 1.390000, 'Liquid Helium': 1.025000, 'Plate Glass (window glass)': 1.520000, 'Polycabonate': 1.600000, 
     'Sapphire': 1.770000, 'Silicon': 3.450000, 'Sodium Chloride (table salt)': 1.544000, 'Vacuum': 1.000000, 'Water': 1.330000, 'Water Ice': 1.310000
}


with header:
    st.title('Welcome to the Light Refraction Calculator')
    # st.title('Welcome to the Refraction of Light Calculator')
    
    htp = "kelly_frisby_physics.jpg"
    st.image(htp, caption= 'logo', width=350)
    #image = Image.open(refraction_image)
    
    kelly_frisby = "https://github.com/kjfrisby/Refraction/blob/main/Refraction_light.svg.png"
    st.image(kelly_frisby, caption= 'logo', width=350)
    #st.image(image, caption='Light ray refraction (By ajizai - https://commons.wikimedia.org/w/index.php?curid=30455241)', output_format="PNG")
       
    # st.text('')
    
    st.markdown("Introducing the Refraction of Light Calculator that will help you calculate the refraction angles as light passes through multiple substances. It uses [Snell's law](https://en.wikipedia.org/wiki/Snell%27s_law) to make the calculations and has been developed to help you understand optics and the wave nature of light better.", unsafe_allow_html=True)
    st.markdown("Simply select the substances through which a ray of light is passing, and let the calculator do the rest.")
    st.write('  ')
    #st.markdown("<h4 style='text-align: center; color: #444444;'>I created the Light Refraction Calculator, using the Python programming language and Streamlit, to help people study the physics and mathematics of light refraction</h4>", unsafe_allow_html=True)
    colx, coly, colz = st.columns([4, 5, 4])
    #image = Image.open('c:/Users/Kelly/kelly_frisby_physics.jpg')
    #coly.image(image, output_format="JPG", use_column_width=True)
    st.markdown('"_I_ _created_ _the_ _Light_ _Refraction_ _Calculator_ _using_ _the_ _Python_ _programming_ _language_ _and_ _Streamlit_ _to_ _help_ _people_ _study_ _the_ _physics_ _and_ _mathematics_ _of_ _light_ _refraction_."')
    st.markdown('**Kelly Frisby, Maths, Physics and Python Enthusiast**')
    st.write('  ')
    
    


with substance_1:
    st.title('Select Your Substances and Calculate Refraction Statistics')
    sel_col2, disp_col2 = st.columns(2)
    sel_col2.subheader('Substance 1')
    sel_col2.write("  ")
    
    #Selectbox for user to select first substance through which light travels
    substance_1 = sel_col2.selectbox('Select first substance light ray passes through:', options=['Acetone', 'Acrylic Glass', 'Air', 'Amber', 'Benzene', 'Bromine', 'Carbon Dioxide', 
    'Corn Oil', 'Crown Glass (pure)', 'Cubic Zirconia', 'Diamond', 'Ethanol', 'Film (transparent)', 'Flint Glass (pure)', 'Germanium', 'Glycerol', 'Helium', 'Hydrogen', 'Kerosene', 'Liquid Helium', 
    'Plate Glass (window glass)', 'Polycabonate', 'Sapphire', 'Silicon', 'Sodium Chloride (table salt)', 'Vacuum', 'Water', 'Water Ice'], index=2)
    RI_sub1 = RI_Dict.get(substance_1)
    #Get value from substance select box and return substance name
    if substance_1 != 'None':
        RI_sub1 = RI_Dict.get(substance_1)    
    
    #Display Refractive Index of Substance 1
        st.write('Refraction Index of Substance 1 is', RI_sub1)
    
    #Calculate and display the speed of light in substance 1. Remember RI, n = (speed of light in vacuum)/(speed of light in transparent substance)
        SoL_1 = 3*10**8/RI_sub1
        st.write('Speed of Light in Substance 1 (m/s) =', SoL_1)

    #Enable user to input angle of incidence from the normal (to the boundary with substance 2) in substance 1
        sel_col2.write('**Select the Angle of Incidence**')
        input_degrees = sel_col2.number_input('What is the angle of incidence of the light ray (in degrees from the normal) as it crosses the boundary from substance 1 to substance 2?', min_value=0, max_value=90)
        
    #Calculate sine of angle of incidence in degrees
        sine_AoI = math.sin(math.radians(input_degrees))                                      #sin of angle of incidence in degrees
    
    #Create space to improve GUI design
        sel_col2.write('  ')

        disp_col2.write('  ')
        disp_col2.write('  ')
        disp_col2.write('  ')
    
    #Display to user the Sine of the angle of incidence
        st.write('The Sine of the Angle of Incidence is:', sine_AoI)
     
        
    
with substance_2: 
    st.subheader('Substance 2')
    sel_col3, disp_col3 = st.columns(2)
   
    substance_2 = sel_col3.selectbox('Select second substance light ray passes through:',options=['Acetone', 'Acrylic Glass', 'Air', 'Amber', 'Benzene', 'Bromine', 'Carbon Dioxide', 
    'Corn Oil', 'Crown Glass (pure)', 'Cubic Zirconia', 'Diamond', 'Ethanol', 'Film (transparent)', 'Flint Glass (pure)', 'Germanium', 'Glycerol', 'Helium', 'Hydrogen', 'Kerosene', 'Liquid Helium', 
    'Plate Glass (window glass)', 'Polycabonate', 'Sapphire', 'Silicon', 'Sodium Chloride (table salt)', 'Vacuum', 'Water', 'Water Ice'], index=26)
    RI_sub2 = RI_Dict.get(substance_2)
    # input_degrees = sel_col2.number_input('What is the angle of incidence of the light ray (in degrees from the normal) as it crosses the boundary from substance 1 to substance 2?', min_value=0, max_value=90)
   
    sine_AoI = math.sin(math.radians(input_degrees))  
    #If substance 1 and/or 2 is showing a value of None, ask user to select substances for 1 and 2
    if substance_1 == 'None' or substance_2 == 'None':
        st.write('Please ensure you have selected options for both Substance 1 and Substance 2, for refraction calculation in Substance 2')
        
    #If user has selected values for Substance 1 and Substance 2, complete following commands
    #If Substance 2 is not None, get Refractive Index number of Substance 2 and write it to GUI
    elif substance_2 != 'None':
        RI_sub2 = RI_Dict.get(substance_2)
        st.write('Refraction Index of Substance 2 is', RI_sub2)
    
    sine_AoR_Sub2 = (RI_sub1*sine_AoI)/RI_sub2
   
    if RI_sub2 == RI_sub1:
          st.write('Substance 1 and Substance 2 have the same refractive index. Therefore, the light ray from Substance 1 passes into Substance 2 with no refraction. Use Snells Law to confirm this.')



     
#if n1 is less than n2, proceed to calculate angle of refraction in substance 2 as TIR will not occur (TIR occurs when n1 is greater than n2. n1 and n2 are the Refractive Indices RI_sub1 etc)        
    if RI_sub1 < RI_sub2:
       # st.write(RI_sub1)
       # st.write(sine_AoI)
       # st.write(RI_sub2)
       sine_AoR_Sub2 = RI_sub1*sine_AoI/RI_sub2
       st.write('Sine of angle of refraction in substance 2 =', sine_AoR_Sub2)
       inv_sine_AoR_sub2 = math.asin(sine_AoR_Sub2)
       st.write('Based on your selection of Substance 2, the angle of refraction in Substance 2 =', inv_sine_AoR_sub2*180/math.pi)       
          
       #Calculate and display the speed of light in substance 2. Remember RI, n = (speed of light in vacuum)/(speed of light in transparent substance)
       SoL_2 = 3*10**8/RI_sub2
       st.write('Speed of Light in Substance 2 (m/s) =', SoL_2)
       
    elif RI_sub1 > RI_sub2:
           sine_crit_ang_sub1 = RI_sub2/RI_sub1     
           #inverse sine (angle) in radians
           inv_sine_crit_ang_sub1 = math.asin(sine_crit_ang_sub1)
           #inverse sine (angle) in degrees
           inv_sine_crit_ang_sub1_degs = inv_sine_crit_ang_sub1*180/math.pi
           st.write('Based on your selection of Substance 2, the critical angle at the boundary of Substance 1 with Substance 2 =', inv_sine_crit_ang_sub1_degs) 
           if input_degrees > inv_sine_crit_ang_sub1_degs:
               st.write('You have input an angle of incidence in substance 1 that is greater than the critical angle at the boundary between Substance 1 and Substance 2. Therefore, Total Internal Reflection (TIR) has occured in your selected Substance 1 and no light has passed into Substance 2, resulting in no refraction of light taking place in Substance 2. Input an angle of incidence in Substance 1 that is less than the critical angle to see refraction occur in Substance 2.')
        
           if input_degrees == inv_sine_crit_ang_sub1_degs:
               st.write('You have input an angle of incidence in Substance 1 that is equal to the critical angle in Substance 1. Light has refracted at a 90 degree angle along the boundary with substance 2, with partial reflection in Substance 1 also occuring.')
        
           if input_degrees < inv_sine_crit_ang_sub1_degs:
               sine_AoR_Sub2 = RI_sub1*sine_AoI/RI_sub2
               st.write('Sine of angle of refraction in substance 2 =', sine_AoR_Sub2)
               inv_sine_AoR_sub2 = math.asin(sine_AoR_Sub2)
               st.write('Based on your selection of Substance 2, the angle of refraction in Substance 2 =', inv_sine_AoR_sub2*180/math.pi)       
          
       #Calculate and display the speed of light in substance 2. Remember RI, n = (speed of light in vacuum)/(speed of light in transparent substance)
               SoL_2 = 3*10**8/RI_sub2
               st.write('Speed of Light in Substance 2 (m/s) =', SoL_2)
     

               
               
               
       
with substance_3:
    st.subheader('Substance 3')
    sel_col4, disp_col4 = st.columns(2)
    substance_3 = sel_col4.selectbox('Select the third substance:', options=['Acetone', 'Acrylic Glass', 'Air', 'Amber', 'Benzene', 'Bromine', 'Carbon Dioxide', 
    'Corn Oil', 'Crown Glass (pure)', 'Cubic Zirconia', 'Diamond', 'Ethanol', 'Film (transparent)', 'Flint Glass (pure)', 'Germanium', 'Glycerol', 'Helium', 'Hydrogen', 'Kerosene', 'Liquid Helium', 
    'Plate Glass (window glass)', 'Polycabonate', 'Sapphire', 'Silicon', 'Sodium Chloride (table salt)', 'Vacuum', 'Water', 'Water Ice'], index=10)
    sine_AoR_Sub2 = sine_AoI/RI_sub2
    inv_sine_AoR_sub2 = math.asin(sine_AoR_Sub2)
    t = inv_sine_AoR_sub2*180/math.pi 
    
    
    RI_sub3 = RI_Dict.get(substance_3)
    sine_AoR_Sub2 = RI_sub1*sine_AoI/RI_sub2
    
    if substance_3 != 'None':
        RI_sub3 = RI_Dict.get(substance_3)
        st.write('Refraction Index of Substance 3 is', RI_sub3)
    # RI_sub1 = RI_Dict.get(substance_1)
    if RI_sub1 > RI_sub2:
        sine_crit_ang_sub1 = RI_sub2/RI_sub1     
         # st.write(sine_crit_ang_sub1)
    # #inverse sine (angle) in radians
        inv_sine_crit_ang_sub1 = math.asin(sine_crit_ang_sub1)
    # #inverse sine (angle) in degrees
        inv_sine_crit_ang_sub1_degs = inv_sine_crit_ang_sub1*180/math.pi
    
    #     if input_degrees > inv_sine_crit_ang_sub1_degs:
    #         st.write('Total Internal Reflection in Substance 1 has occured resulting in no light passing from Substance 2 into Substance 3 and therefore no refraciton of light in Substance 3. Please change your selections to see light refraction in Substance 3.')

    
        if input_degrees < inv_sine_crit_ang_sub1_degs:
        
            #If substance 1 and/or 2 is showing a value of None, ask user to select substances for 1 and 2
            # if substance_3 == 'None' or substance_2 == 'None' or substance_1 == 'None':
            #     st.write('Please ensure you have selected options for Substance 1, Substance 2, and Substance 3, for refraction calculation in Substance 3')
        
        
            # elif substance_3 != 'None':
            #Get user input Substance 3 value, look up that substance in the dictionary (see top of page) and return and write the Refractive Index value
                RI_sub3 = RI_Dict.get(substance_3)
                st.write('Refraction Index of Substance 3 is', RI_sub3)        
          
            # if RI_sub2 < RI_sub3:
                sine_AoR_Sub3 = RI_sub2*sine_AoR_Sub2/RI_sub3
                inv_sine_AoR_sub3 = math.asin(sine_AoR_Sub3)
                st.write('Based on your selection of Substance 2, the angle of refraction in Substance 3 =', inv_sine_AoR_sub3*180/math.pi) 
                #Calculate and display the speed of light in substance 2. Remember RI, n = (speed of light in vacuum)/(speed of light in transparent substance)
                SoL_3 = 3*10**8/RI_sub3
                st.write('Speed of Light in Substance 3 (m/s) =', SoL_3)
                
                
                   #the sine of the angle of refraction in substance 2 is equal to the sine of the angle of incidence as the ray crosses boundary into substance 3 (due to laws of trigonometry) 
                   # sine_AoI_Sub2 = sine_AoR_Sub2
        
        if input_degrees >= inv_sine_crit_ang_sub1_degs:
            st.write('Light has not passed into substance 2 and therefore has not passed into Substance 3. Please change your selections to see refraction in Substance 3.')
      
    elif RI_sub2 > RI_sub3:
        sine_crit_ang_sub2 = RI_sub3/RI_sub2     
        # st.write(sine_crit_ang_sub2)
        inv_sine_crit_ang_sub2 = math.asin(sine_crit_ang_sub2)
        # st.write(inv_sine_crit_ang_sub2)
        inv_sine_crit_ang_sub2_degs = inv_sine_crit_ang_sub2*180/math.pi
        # st.write(inv_sine_crit_ang_sub2_degs)
        st.write('Based on your selection of Substance 2, the critical angle at the boundary of Substance 2 with Substance 3 =', inv_sine_crit_ang_sub2_degs) 
        sine_AoR_Sub2 = (RI_sub1*sine_AoI)/RI_sub2
        # st.write(sine_AoR_Sub2)
        inv_sine_AoR_sub2 = math.asin(sine_AoR_Sub2)
        t = inv_sine_AoR_sub2*180/math.pi 
        # st.write(t)
        if t > inv_sine_crit_ang_sub2_degs:
            st.write('The angle of incidence in substance 2 is greater than the critical angle at the boundary between Substance 2 and Substance 3. Therefore, Total Internal Reflection (TIR) has occured in Substance 2 and no light has passed into Substance 3, resulting in no refraction of light taking place in Substance 3.')
        if t < inv_sine_crit_ang_sub2_degs:
        # if inv_sine_crit_ang_sub2_degs == inv_sine_crit_ang_sub1_degs:
        #     st.write('The angle of incidence in Substance 2 is equal to the critical angle at the boundary between Substance 2 and Substance 3. The result is that light has refracted at a 90 degree angle along the boundary with substance 3, with partial reflection in Substance 2 also occuring and no light has passed into Substance 3.')
            sine_AoR_Sub3 = RI_sub2*sine_AoR_Sub2/RI_sub3
            inv_sine_AoR_sub3 = math.asin(sine_AoR_Sub3)
            st.write('Based on your selection of Substance 2, the angle of refraction in Substance 3 =', inv_sine_AoR_sub3*180/math.pi) 
            #Calculate and display the speed of light in substance 2. Remember RI, n = (speed of light in vacuum)/(speed of light in transparent substance)
            SoL_3 = 3*10**8/RI_sub3
            st.write('Speed of Light in Substance 3 (m/s) =', SoL_3)
        
        if t == inv_sine_crit_ang_sub2_degs:
           st.write('The an angle of incidence in Substance 2 is equal to the critical angle in Substance 2. Light has refracted at a 90 degree angle along the boundary with substance 1, with partial reflection in Substance 2 also occuring.')
      
    elif RI_sub3 == RI_sub2:
       st.write('Substance 2 and Substance 3 have the same refractive index. Therefore, the light ray from Substance 2 passes into Substance 3 with no refraction. Use Snells Law to confirm this.')
  
    elif RI_sub2 < RI_sub3:
       sine_AoR_Sub3 = RI_sub2*sine_AoI/RI_sub3
       st.write('Sine of angle of refraction in substance 3 =', sine_AoR_Sub3)
       inv_sine_AoR_sub3 = math.asin(sine_AoR_Sub3)
       st.write('Based on your selection of Substance 2, the angle of refraction in Substance 3 =', inv_sine_AoR_sub3*180/math.pi)       
              
       #Calculate and display the speed of light in substance 2. Remember RI, n = (speed of light in vacuum)/(speed of light in transparent substance)
       SoL_3 = 3*10**8/RI_sub3
       st.write('Speed of Light in Substance 3 (m/s) =', SoL_3)
       st.write('')
       st.write('')
       st.write('')
       
      
with refraction_boundaries:
    st.header('Understanding the Physics of Light Refraction')
    st.write('')
    st.write('')
    #image = Image.open("c:/Users/Kelly/refraction light multiple.png")    
                                                      #image from https://xaktly.com/Refraction.html
    #col1, col2, col3 = st.columns([4, 5, 4])
    #col2.image(image, caption='Multiple Substance Refraction of Light', output_format="PNG", use_column_width=True)             #image from https://xaktly.com/Refraction.html
    #st.image(image, caption='Multiple Substance Refraction of Light', output_format="PNG")
    st.write('')
    st.write('')  
    
    st.markdown("The Multiple Substance Refraction Calculator calculates the angles of refraction of a light ray as it passes the boundary of one substance to another. It uses [Snell's law](https://en.wikipedia.org/wiki/Snell%27s_law):", unsafe_allow_html=True) 
    st.latex(r'''
         {n}_1sin(\theta_1) = {n}_2sin(\theta_2)
         ''')
    st.markdown("Where:")
    st.latex(r'''
         {n}_1 = Refraction\ Index\ of\ Substance\ 1
         ''')
    st.latex(r'''
         {n}_2 = Refraction\ Index\ of\ Substance\ 2
              ''')
    st.latex(r'''
         \theta_1 = Angle\ of\ Incidence\ (in\ Substance\ 1)
          ''') 
    st.latex(r'''
         \theta_2 = Angle\ of\ Refraction\ (in\ Substance\ 2)
                ''')    
    
    
    st.write('')

    st.write('Rearranging the formula, we can determine the angle of refraction when a light ray crosses the boundary from the first substance to the second substance:')


    st.latex(r'''
         Angle\ of\ Refraction,\ \theta_2 = sin^{-1} \left(\frac{{n}_1sin(\theta_1)}{{n}_2}\right) 
         ''')
        
      
        
      
        
      
        
      
        
      
        # Convert critical angle in radians to degrees and output to User in GUI
        # st.write('Based on your selection of Substance 2, the critical angle of Substance 1 =', inv_sine_crit_1*180/math.pi)
        
        # Calculate sine of angle of refraction in Substance 2
       # sine_AoR = RI_sub1*sine_AoI/RI_sub2
        
        # If statements for whether sine of angle of refraction is less than, equal to, or greater than 1. If sine of refraction angle greater than 1 (sin90), then no refraction in substance 2 takes place as TIR has occurred in Substance 1
        # if sine_AoR < 1:
        #     st.write('Sine of the Angle of Refraction =', sine_AoR)
        #     inv_sine_AoR = math.asin(sine_AoR)
        #     st.write('Angle of Refraction in degrees = ', inv_sine_AoR*180/math.pi)
        # if sine_AoR == 1:
        #     st.write('Sine of the Critical Angle of Refraction =', sine_AoR)
        #     inv_sine_AoR = math.asin(sine_AoR)
        #     st.write('Angle of Refraction in degrees = ', inv_sine_AoR*180/math.pi)
        # if sine_AoR > 1:
        #     st.write('Since Substance 2 has a lower refractive index than Substance 1, and your selected *angle of incidence* in Substance 1 is greater than the critical angle, [Total Internal Reflection (TIR)](https://isaacphysics.org/concepts/cp_reflection_and_refraction?stage=all) in Substance 1 has occurred, meaning the light ray in Substance 1 has not passed the boundary into Substance 2. Please select an angle of incidence in Substance 1 that is less than the critical angle, to calculate light refraction in Substance 2.', unsafe_allow_html=True)

        
        
        
        
        # #Calculate the inverse sine value in radians of the sine of the angle of refraction
        # inv_sine_AoR = math.asin(sine_AoR)
        
        # #Calculate and display the speed of light in substance 3. Remember RI, n = (speed of light in vacuum)/(speed of light in transparent substance)
        # SoL_3 = 3*10**8/RI_sub3
        # st.write('Speed of Light in Substance 3 (m/s) =', SoL_3)
        
        # #Calculate the angle of incidence in substance 2 in degrees
        # AoI_in_Sub2 = inv_sine_AoR*180/math.pi
        
        # # st.write('Angle of Incidence in degrees =', AoI_in_Sub2)
        # sine_AoI_in_sub2 = math.sin(math.radians(AoI_in_Sub2))
        
        # # st.write('Sine of the Angle of Incidence in degrees = ', sine_AoI_in_sub2)
        # sine_AoR_sub3 = RI_sub2*sine_AoI_in_sub2/RI_sub3
        # st.write('Sine of the Angle of Refraction in degrees = ', sine_AoR_sub3)
    
        # #inverse sine of angle of refraction in substance 3 (in radians)
        # inv_sine_AoR_sub3 = math.asin(sine_AoR_sub3)
        # st.write('Angle of Refraction in degrees = ', inv_sine_AoR_sub3*180/math.pi)
    
    # else:
    #     st.write('Please select Substance 3')


# #Notes:
# st.latex(r'''
#       a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#       \sum_{k=0}^{n-1} ar^k =
#       a \left(\frac{1-r^{n}}{1-r}\right)
#       ''')
    
  
# For light that passes from a medium with a higher refractive index to one with a lower refractive index, there is a critical angle of incidence above which all light is reflected. 
# This phenomenon is called total internal reflection.


    
    
    
