package com.llq.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.llq.entity.Student;
import com.llq.mapper.StudentMapper;
import com.llq.service.StudentService;

@Service
public class StudentServiceImpl implements StudentService {
	
	@Autowired
	private StudentMapper studentMapper;

	@Override
	public Student findStudentById(Integer id) {
		System.out.println("--> Student com.llq.service.impl.StudentServiceImpl.findStudentById(Integer id)");
		return studentMapper.findStudentById(id);
	}

}
