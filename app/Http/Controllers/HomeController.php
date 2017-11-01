<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Data;
	
class HomeController extends Controller
{
    public function Trend(){
        $data = Data::limit(12)->where('CATEGORY','=','1')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }

    public function Entertainment(){
        $data = Data::limit(12)->where('CATEGORY','=','2')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }

    public function Intermezo(){
        $data = Data::limit(12)->where('CATEGORY','=','3')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }

    public function Inspirasi(){
        $data = Data::limit(12)->where('CATEGORY','=','4')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }

    public function Olahraga(){
        $data = Data::limit(12)->where('CATEGORY','=','5')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }

    public function Tips(){
        $data = Data::limit(12)->where('CATEGORY','=','6')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }

    public function Travel(){
        $data = Data::limit(12)->where('CATEGORY','=','7')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }

    public function Unikaneh(){
        $data = Data::limit(12)->where('CATEGORY','=','8')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }

    public function English(){
        $data = Data::limit(12)->where('CATEGORY','=','0')->orderBy('ID', 'desc')->get();
        return view('home', ['data' => $data]);
    }
}
