SetFactory("OpenCASCADE");

Circle(1) = {0, 0, 0, 0.5};
Curve Loop(2) = {1};
Plane Surface(1) = {2};
Rectangle(2) = {-10, -5, 0, 20, 10};
BooleanDifference(3) = {Surface{2}; Delete;} {Surface{1}; Delete;};

Transfinite Curve {5} = 100;
Transfinite Curve {1,4} = 40;
Transfinite Curve {2,3} = 20;

Mesh 1;
Mesh 2;

Physical Curve("Inlet", 1) = {2};
Physical Curve("Outlet", 2) = {3};
Physical Curve("Top", 3) = {4};
Physical Curve("Bottom", 4) = {1};
Physical Curve("Wall", 5) = {5};
Physical Surface("Fluid", 6) = {3};

Mesh.Format = 1;
Mesh.MshFileVersion = 2.2; 
Mesh.SaveAll = 0;
Mesh.Binary = 0;

//Save "example.msh";