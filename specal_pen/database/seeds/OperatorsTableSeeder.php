<?php

use Illuminate\Database\Seeder;

class OperatorsTableSeeder extends Seeder
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
            '/',
        ];
        for($i=0; $i<100; $i++) {
            shuffle($operators);
            \App\Operator::create([
                'operators' => $operators[0],
            ]);
        }
    }
}
