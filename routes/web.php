<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/trend', 'HomeController@Trend');
Route::get('/entertainment', 'HomeController@Entertainment');
Route::get('/intermezo', 'HomeController@Intermezo');
Route::get('/inspirasi', 'HomeController@Inspirasi');
Route::get('/olahraga', 'HomeController@Olahraga');
Route::get('/tips', 'HomeController@Tips');
Route::get('/travel', 'HomeController@Travel');
Route::get('/unikaneh', 'HomeController@Unikaneh');
Route::get('/english', 'HomeController@English');