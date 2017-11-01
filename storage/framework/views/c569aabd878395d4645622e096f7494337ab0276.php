<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="<?php echo e(URL::asset('/bootstrap/css/bootstrap.min.css')); ?>">
    <style>
    	.center{text-align: center !important;}
	</style>
  </head>
  <body>
  <div class="container">
      	<div class="jumbotron">
    		<h1>News Aggregator</h1>
	    </div>
	    <div class="row">
	    	<div class="col-md-10 col-md-offset-1">
			    <div class="navbar navbar-default">
			    	<div class="container-fluid">
			    		<div class="navbar-header">
				    		<ul class="nav navbar-nav">
							  <li class="col-md-offset-1"> </li>	
							  <li role="presentation" class="<?php if(URL::current() == URL::to('/trend')): ?> active <?php endif; ?> col-md-2"><a href="trend">Trend</a></li>
							  <li role="presentation" class="<?php if(URL::current() == URL::to('/unikaneh')): ?> active <?php endif; ?> col-md-2"><a href="unikaneh">Unik &amp; Aneh</a></li>
							  <li role="presentation" class="<?php if(URL::current() == URL::to('/intermezo')): ?> active <?php endif; ?> col-md-2"><a href="intermezo">Intermezo</a></li>
							  <li role="presentation" class="<?php if(URL::current() == URL::to('/entertainment')): ?> active <?php endif; ?> col-md-2"><a href="entertainment">Entertainment</a></li>
							  <li role="presentation" class="<?php if(URL::current() == URL::to('/tips')): ?> active <?php endif; ?> col-md-2"><a href="entertainment">Entertainment</a></li>
							  <li role="presentation" class="<?php if(URL::current() == URL::to('/travel')): ?> active <?php endif; ?> col-md-2"><a href="travel">Travel</a></li>
							  <li role="presentation" class="<?php if(URL::current() == URL::to('/inspir	asi')): ?> active <?php endif; ?> col-md-2"><a href="inspirasi">Inspirasi</a></li>
							  <li role="presentation" class="<?php if(URL::current() == URL::to('/olahraga')): ?> active <?php endif; ?> col-md-2"><a href="olahraga">Olahraga</a></li>
							  <li class="col-md-offset-1"></li>
							</ul>
						</div>
					</div>
		    	</div>
			</div>		    	
	    </div>