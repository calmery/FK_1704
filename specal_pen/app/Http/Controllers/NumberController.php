<?php

namespace App\Http\Controllers;

use DB;
use Input;
use \App\Calculation;
use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class NumberController extends Controller
{
    //データベースから計算を受け取って出力する
    public function index()
    {
        $numbers = DB::table('calculations')->get();
        return view('number', ['numbers' => $numbers]);
    }
    //formからリクエストを受け取ってテーブルに挿入する
    public function insert(Request $request)
    {
        $num_l = intval($request->input('num-l'));
        $ope = $request->input('ope');
        $num_r = intval($request->input('num-r'));
        $answer = intval($request->input('ans'));
        
        DB::table('calculations')->insert(
    ['number_l' => $num_l, 'operators' =>$ope,'number_r' => $num_r,'answer' => $answer]
);
        //ビューの表示にリダイレクトする
        return redirect()->action('NumberController@index');
    }

    
}
