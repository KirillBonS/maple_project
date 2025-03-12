Код решения и результат Maple:
f := (x, y) -> x*sin(y^2);
plot3d(f(x, y), x = -2.5 .. 2.5, y = -2.5 .. 2.5, orientation = [60, 60]);]);
![изображение](https://github.com/user-attachments/assets/ef031f20-2633-4bf2-b4e2-dccdd851ae56)
> plot3d(f(x, y), x = -2.5 .. 2.5, y = -2.5 .. 2.5, orientation = [90, 90, 0]);
> ![изображение](https://github.com/user-attachments/assets/e280a69b-7743-4519-ac80-c811c6e3a5e7)
>plot3d(f(x, y), x = -2.5 .. 2.5, y = -2.5 .. 2.5, orientation = [180, 180]);
> ![изображение](https://github.com/user-attachments/assets/7526b61c-d160-4d85-80e7-b3bee9b31c03)
Вывод:
На Python и Maple возможно построить необходимые поверхности. Также при выполнении подобных задач возможности Python достаточны и не отличаются от возможностей Maple
