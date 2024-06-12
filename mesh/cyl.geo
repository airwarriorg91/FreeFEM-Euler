// Cylinder @ Re=40 Mesh designed for FreeFEM++
SetFactory("OpenCASCADE");

h = 3;
w = 3;
nc = 0.05;
nd = 0.5;
//Boundary Points
Point(1) = {0, 0, 0, 1.0};
Point(2) = {-3, h, 0, nd};
Point(3) = {-3, -h, 0, nd};
Point(4) = {w, -h, 0, nd};
Point(5) = {w, h, 0, nd};
Point(8) = {0.5*Cos(45*Pi/180), 0.5*Sin(45*Pi/180), 0, nc};
Point(9) = {0.5*Cos(135*Pi/180), 0.5*Sin(135*Pi/180), 0, nc};
Point(10) = {0.5*Cos(135*Pi/180), -0.5*Sin(135*Pi/180), 0, nc};
Point(11) = {0.5*Cos(45*Pi/180), -0.5*Sin(45*Pi/180), 0, nc};

//cylinder
Circle(1) = {8, 1, 9}; // 45 --> 135
Circle(2) = {9, 1, 10}; // 135 --> 225
Circle(3) = {10, 1, 11}; // 225 --> 315 
Circle(4) = {11, 1, 8}; //315 --> 45

//domain boundaries
Line(5) = {2, 5}; //top
Line(7) = {5, 4}; //outlet
Line(8) = {4, 3}; //bottom
Line(10) = {3, 2}; //inlet

//surface
Curve Loop(1) = {10, 5, 7, 8};
Curve Loop(2) = {2, 3, 4, 1};
Plane Surface(1) = {1, 2};

Extrude {0, 0, 0.5} {
   Surface{1}; Layers{3};
}


Physical Surface("Inlet", 1) = {2};
Physical Surface("Outlet", 2) = {4};
Physical Curve("top1", 3) = {15};
Physical Curve("top2", 4) = {5};
Physical Curve("bottom1", 5) = {18};
Physical Curve("bottom2", 6) = {8};
Physical Surface("Cylinder", 7) = {7, 8, 9, 6};
Physical Volume("Fluid", 8) = {1};
Physical Surface("Top", 9) = {3};
Physical Surface("Bottom", 10) = {5};
Physical Surface("Front", 11) = {10};
Physical Surface("Back", 12) = {1};

Mesh 1;
Mesh 2;
Mesh 3;

RenumberMeshElements;

Mesh.Format = 1;
Mesh.MshFileVersion = 2.2; 
Mesh.SaveAll = 0;
Mesh.Binary = 0;

Save "cyl.msh";




