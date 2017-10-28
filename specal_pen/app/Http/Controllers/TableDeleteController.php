<?php

namespace App\Http\Controllers;

use DB;
use \App\Calculation;
use Illuminate\Http\Request;

class TableDeleteController extends Controller
{
    //
     public function index()
    {
        DB::table('calculations')->delete();
        return redirect()->action('NumberController@index');
    }
}
