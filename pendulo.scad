base_largura            = 30;
base_comprimento        = 80;
base_altura             = 17;
furo_sensor_largura     = 12;
furo_sensor_comprimento = 07;
torre_largura           = 10;
torre_altura            = 120;
topo_comprimento        = 50;
topo_altura             = 10;

$fn=50;

module base(){   
    difference(){
        cube([base_comprimento,base_largura,base_altura], center = true);
        
        translate([base_comprimento/2 - (furo_sensor_comprimento + 1),0,1])
            cube([furo_sensor_comprimento,furo_sensor_largura,base_altura], center = true);
        
        translate([-base_comprimento/2 -1,-12,-base_altura/2 - 0.01])
        rotate(a=90,v=[1,0,0])
        rotate(a=90,v=[0,1,0])
        linear_extrude(height = base_comprimento + 2)
            polygon(points=[[0,0],[4.5,10],[19.5,10],[24,0]]);
    }    
}

module torre(){
    translate([-base_comprimento/2 + base_largura,0,torre_altura/2 + base_altura/2 - 0.01])
        cube([torre_largura,base_largura,torre_altura], center = true);
}

module topo(){
    difference(){
        translate([-base_comprimento/2 + topo_comprimento + torre_largura -0.01,0,torre_altura+3.5])
            cube([topo_comprimento+0.01,base_largura,topo_altura], center = true);
        
        translate([base_comprimento/2 - (furo_sensor_comprimento + 1),0,torre_altura+topo_altura - 7])
            cylinder(d=3, h=topo_altura+5,center=true);
    }
}


base();
torre();
topo();

