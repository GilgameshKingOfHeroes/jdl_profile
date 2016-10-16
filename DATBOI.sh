#!/bin/bash

title="System Information Page: Kirei Kotomine edition"
FavDrink="TabascoSauce"
FavActivity="Making others suffer and drinking their tears of sadness"

cat << BLACK_KEYS
<html>
	<head>
		<title>$title</title>
	</head>
	<body>
		<h1>$title</h1>
		<h2>Kirei Kotomine's SEIHAI computer</h2>
		<p>User who uses this computer</p>
		<pre>$USER</pre>
		<p>What shell he uses</p>
		<pre>$SHELL</pre>
		<p>His Favorite drink</p>
		<pre>$FavDrink</pre>
		<p>His favorite activity</p>
		<pre></pre
		<p>How many evil plans he has on storage</p>
		<pre>$(ls -l ~)</pre>
		<p>How much space he has</p>
		<pre>$(df -h)</pre>
		<p>When this was created</p>
		<pre>$(date)</pre>
BLACK_KEYS
