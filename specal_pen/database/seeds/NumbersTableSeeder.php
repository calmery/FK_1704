<?php

use Illuminate\Database\Seeder;

class NumbersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        //
        for($i=0; $i<100; $i++) {
            \App\Number::create([
                'number_l' => random_int(1,10),
                'number_r' => random_int(1, 10),
            ]);
        }
    }
}
