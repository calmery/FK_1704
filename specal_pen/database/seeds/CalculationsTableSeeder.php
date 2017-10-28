<?php

use Illuminate\Database\Seeder;

class CalculationsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        //
        $operators = [
            '+',
            '-',
            '*',
        ];
        for($i=0; $i<100; $i++) {
            shuffle($operators);
            \App\Calculation::create([
                'number_l' => random_int(1,10),
                'operators' => $operators[0],
                'number_r' => random_int(1, 10),
                'answer' => random_int(1, 10),
            ]);
        }
    }
}
