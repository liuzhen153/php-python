<?php
namespace app\index\controller;
use ppython\Ppython;

class Index
{
    // 不带参数
    public function py()
    {
		$python = new Ppython();
	    $data = $python->py("sayhi.hi::hello");
	    dump($data);
    }

    //带参数的方法
    public function py_with_something($name)
    {
		$python = new Ppython();
        // 更多参数依次往后添加
	    $data = $python->py("sayhi.hi::hello_name",$name);
	    dump($data);
    }

	// python返回的是数组
	public function py_arr()
	{
		$python = new Ppython();
	    $data = $python->py("sayhi.hi::return_arr");
	    dump($data);
	}

	// PHP传递数字类型变量，计算2+3的和
	public function py_num()
	{
		$python = new Ppython();
	    $data = $python->py("sayhi.hi::dosum",2,3);
	    dump($data);
	}
}
