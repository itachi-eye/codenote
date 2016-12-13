package com.llq.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.llq.entity.Student;
import com.llq.service.StudentService;

@Controller
public class StudentController {

	@Autowired
	private StudentService studentService;

	@RequestMapping("/getstudent")
	public String getStudent(@RequestParam("id") Integer id, Model model) {
		System.out.println("--> in com.llq.controller.StudentController.getStudent");
		Student stu = studentService.findStudentById(id);

		model.addAttribute("student", stu);

		return "result";
	}
}
