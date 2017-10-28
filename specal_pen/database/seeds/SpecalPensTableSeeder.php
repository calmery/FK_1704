<?php

use Illuminate\Database\Seeder;

class SpecalPensTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $operators = [
            '+',
            '-',
            '*',
            '/',
        ];
        for($i=0; $i<100; $i++) {
            shuffle($operators);
            \App\SpecalPen::create([
                'numbers' => (string)random_int(1,10) . $operators[0] . (string)random_int(1, 10),
            ]);
        }
    }
}
