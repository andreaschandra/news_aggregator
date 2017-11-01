<!-- <!DOCTYPE html>
<html lang="en">
  <head> -->
    <!-- Required meta tags -->
    <!-- <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> -->

    <!-- Bootstrap CSS -->
<!--     <link rel="stylesheet" href="{{ URL::asset('/bootstrap/css/bootstrap.min.css') }}">
  </head>
  <body>
  <div class="container">
      	<div class="jumbotron">
    		<h1>News Aggregator</h1>
	    </div>
	    <div class="row">
	    	<div class="col-md-8 col-md-offset-2">
			    <div class="navbar navbar-default">
			    	<div class="container-fluid">
			    		<div class="navbar-header">
				    		<ul class="nav navbar-nav">
							  <li role="presentation" class="@if(URL::current() == URL::to('/trend')) active @endif"><a href="trend">Trend</a></li>
							  <li role="presentation" class="@if(URL::current() == URL::to('/unikaneh')) active @endif"><a href="unikaneh">Unik &amp; Aneh</a></li>
							  <li role="presentation" class="@if(URL::current() == URL::to('/intermezo')) active @endif"><a href="intermezo">Intermezo</a></li>
							  <li role="presentation" class="@if(URL::current() == URL::to('/entertainment')) active @endif"><a href="entertainment">Entertainment</a></li>
							  <li role="presentation" class="@if(URL::current() == URL::to('/travel')) active @endif"><a href="travel">Travel</a></li>
							  <li role="presentation" class="@if(URL::current() == URL::to('/inspir	asi')) active @endif"><a href="inspirasi">Inspirasi</a></li>
							  <li role="presentation" class="@if(URL::current() == URL::to('/olahraga')) active @endif"><a href="olahraga">Olahraga</a></li>
							</ul>
							<ul class="nav navbar-nav navbar-right">
								<li role="presentation" class="@if(URL::current() == URL::to('/english')) active @endif"><a href="english">English</a></li>
							</ul>
						</div>
					</div>
		    	</div>
			</div>		    	
	    </div> -->
	    @include('header')
		<div class="row">
		<?php foreach($data as $val){ ?>
		  <div class="col-sm-6 col-md-4">
			<div class="thumbnail">
			  <!-- <img src="{{ URL::asset('/img/noimg.jpg') }}" alt="..."> -->
			  <img src="<?php echo $val->IMAGE; ?>" alt="..." width = 100%>
			  <div class="caption">
				<h3><?php echo $val->TITLE; ?></h3>
				<p><?php echo $val->DATE ?></p>
				<p><a href="<?php echo $val->URL ?>" class="btn btn-primary" role="button">Read More</a>
			  </div>
			</div>
		  </div>
		  <?php } ?>
		</div>
    </div>
	@extends('footer')
    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <!-- <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
  </body>
</html> -->